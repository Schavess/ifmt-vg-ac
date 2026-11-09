"""ETL do PPI-molde Comparece MT.

Gera a base analítica (uma linha por município de MT) a partir das fontes oficiais:
- TSE, perfil do eleitorado 2026 (X demográficos);
- TSE, resultados do 1º turno para presidente em 2022 e em 2026 (y e abstenção anterior);
- coordenadas das sedes municipais (IBGE, via repositório kelvins/municipios-brasileiros).

Uso no terminal (na pasta do projeto):
    python etl/etl_comparece_mt.py
Os ZIP do TSE são grandes (o do perfil tem cerca de 400 MB), mas só precisamos do CSV de MT
dentro deles. Por isso o ETL lê o ZIP direto do servidor, baixando só os pedaços que usa
(requisições HTTP com "Range"). Ao todo, são poucos MB. A base sai em `dados/base_analitica.csv`.
"""
from pathlib import Path
import io
import unicodedata
import urllib.request
import zipfile

import numpy as np
import pandas as pd

URL_TSE = 'https://cdn.tse.jus.br/estatistica/sead/odsele'
FONTES = {
    'perfil_2026': (f'{URL_TSE}/perfil_eleitorado/perfil_eleitorado_2026.zip', 'perfil_eleitorado_2026_MT.csv'),
    'resultado_2026': (f'{URL_TSE}/detalhe_votacao_munzona/detalhe_votacao_munzona_2026.zip',
                       'detalhe_votacao_munzona_2026_BRASIL.csv'),
    'resultado_2022': (f'{URL_TSE}/detalhe_votacao_munzona/detalhe_votacao_munzona_2022.zip',
                       'detalhe_votacao_munzona_2022_BRASIL.csv'),
}
URL_COORDENADAS = 'https://raw.githubusercontent.com/kelvins/municipios-brasileiros/main/csv/municipios.csv'
CUIABA = (-15.601, -56.097)            # latitude e longitude da sede de Cuiabá
FAIXAS_16_24 = [1600, 1700, 1800, 1900, 2000, 2124]
FAIXAS_65_MAIS = [6569, 7074, 7579, 8084, 8589, 9094, 9599, 9999]
SUPERIOR_COMPLETO = 8
CABECALHO = {'User-Agent': 'Mozilla/5.0 (ETL didatico PPI GovTech IFMT)'}


class ArquivoRemoto(io.RawIOBase):
    """Arquivo na internet que se comporta como arquivo local: cada leitura baixa só o trecho pedido.

    Assim o `zipfile` lê o índice do ZIP (que fica no fim) e só o membro que nos interessa.
    """
    def __init__(self, url, bloco=1 << 20):
        self.url, self.pos, self.bloco, self.cache = url, 0, bloco, {}
        with urllib.request.urlopen(urllib.request.Request(url, method='HEAD', headers=CABECALHO)) as r:
            self.tamanho = int(r.headers['Content-Length'])

    def seekable(self): return True
    def readable(self): return True
    def tell(self): return self.pos

    def seek(self, deslocamento, origem=io.SEEK_SET):
        base = {io.SEEK_SET: 0, io.SEEK_CUR: self.pos, io.SEEK_END: self.tamanho}[origem]
        self.pos = max(0, base + deslocamento)
        return self.pos

    def _bloco(self, i):
        if i not in self.cache:
            ini, fim = i * self.bloco, min((i + 1) * self.bloco, self.tamanho) - 1
            req = urllib.request.Request(self.url, headers={**CABECALHO, 'Range': f'bytes={ini}-{fim}'})
            with urllib.request.urlopen(req) as r:
                if r.status != 206:
                    raise RuntimeError('o servidor não aceitou leitura por partes; baixe o ZIP e passe o caminho local')
                self.cache = {i: r.read()}          # guarda só o último bloco (memória baixa)
        return self.cache[i]

    def readinto(self, destino):
        n = min(len(destino), self.tamanho - self.pos)
        lidos = 0
        while lidos < n:
            i, off = divmod(self.pos, self.bloco)
            pedaco = self._bloco(i)[off:off + n - lidos]
            destino[lidos:lidos + len(pedaco)] = pedaco
            lidos += len(pedaco); self.pos += len(pedaco)
        return lidos


def ler_csv_do_zip(origem, membro, colunas):
    """Lê só as colunas necessárias de um CSV do TSE (sep ';', latin1) dentro de um ZIP.

    `origem` pode ser um caminho local ou uma URL (lida aos pedaços, sem baixar o ZIP inteiro).
    """
    arquivo = ArquivoRemoto(origem) if str(origem).startswith('http') else origem
    with zipfile.ZipFile(arquivo) as z, z.open(membro) as f:
        return pd.read_csv(io.TextIOWrapper(f, encoding='latin1'), sep=';', usecols=colunas,
                           dtype={'CD_MUNICIPIO': str})


def perfil_por_municipio(perfil):
    """Soma eleitores por município e calcula os percentuais de idade e escolaridade."""
    perfil = perfil.assign(
        N_16_24=perfil['QT_ELEITORES'].where(perfil['CD_FAIXA_ETARIA'].isin(FAIXAS_16_24), 0),
        N_65_MAIS=perfil['QT_ELEITORES'].where(perfil['CD_FAIXA_ETARIA'].isin(FAIXAS_65_MAIS), 0),
        N_SUPERIOR=perfil['QT_ELEITORES'].where(perfil['CD_GRAU_ESCOLARIDADE'] == SUPERIOR_COMPLETO, 0))
    m = perfil.groupby(['CD_MUNICIPIO', 'NM_MUNICIPIO'], as_index=False)[
        ['QT_ELEITORES', 'N_16_24', 'N_65_MAIS', 'N_SUPERIOR']].sum()
    return pd.DataFrame({
        'CD_MUNICIPIO': m['CD_MUNICIPIO'], 'NM_MUNICIPIO': m['NM_MUNICIPIO'],
        'ELEITORADO_PERFIL': m['QT_ELEITORES'],
        'PCT_16_24': 100 * m['N_16_24'] / m['QT_ELEITORES'],
        'PCT_65_MAIS': 100 * m['N_65_MAIS'] / m['QT_ELEITORES'],
        'PCT_SUPERIOR_COMPLETO': 100 * m['N_SUPERIOR'] / m['QT_ELEITORES'],
        'LOG_ELEITORADO': np.log1p(m['QT_ELEITORES'])})


def abstencao_por_municipio(resultado, uf='MT'):
    """Filtra presidente (cargo 1), 1º turno, na UF, e soma aptos e abstenções das zonas."""
    r = resultado[(resultado['SG_UF'] == uf) & (resultado['CD_CARGO'] == 1) & (resultado['NR_TURNO'] == 1)]
    m = r.groupby('CD_MUNICIPIO', as_index=False)[['QT_APTOS', 'QT_ABSTENCOES']].sum()
    m['ABSTENCAO_PCT'] = 100 * m['QT_ABSTENCOES'] / m['QT_APTOS']
    return m


def normalizar_nome(nome):
    """'Mirassol d'Oeste' e 'MIRASSOL D OESTE' viram a mesma chave."""
    sem_acento = unicodedata.normalize('NFKD', nome).encode('ascii', 'ignore').decode()
    return ' '.join(sem_acento.upper().replace("'", ' ').replace('-', ' ').split())


def distancia_km(lat, lon, ref=CUIABA):
    """Distância em linha reta (fórmula de haversine) até o ponto de referência."""
    lat, lon, lat0, lon0 = map(np.radians, (lat, lon, ref[0], ref[1]))
    a = np.sin((lat - lat0) / 2) ** 2 + np.cos(lat) * np.cos(lat0) * np.sin((lon - lon0) / 2) ** 2
    return 2 * 6371 * np.arcsin(np.sqrt(a))


def montar_base(perfil, res_2026, res_2022, coordenadas):
    """Junta as quatro fontes numa linha por município (chave: código TSE)."""
    base = perfil_por_municipio(perfil)
    atual = abstencao_por_municipio(res_2026)
    anterior = abstencao_por_municipio(res_2022).rename(columns={
        'QT_APTOS': 'APTOS_2022', 'QT_ABSTENCOES': 'ABST_2022', 'ABSTENCAO_PCT': 'ABST_2022_PCT'})
    base = base.merge(atual, on='CD_MUNICIPIO', how='inner', validate='1:1')
    base = base.merge(anterior[['CD_MUNICIPIO', 'APTOS_2022', 'ABST_2022_PCT']],
                      on='CD_MUNICIPIO', how='left', validate='1:1')
    base['CRESC_ELEITORADO_PCT'] = 100 * (base['ELEITORADO_PERFIL'] / base['APTOS_2022'] - 1)

    coord = coordenadas[coordenadas['codigo_uf'] == 51].assign(CHAVE=lambda d: d['nome'].map(normalizar_nome))
    base['CHAVE'] = base['NM_MUNICIPIO'].map(normalizar_nome)
    base = base.merge(coord[['CHAVE', 'latitude', 'longitude']], on='CHAVE', how='left', validate='1:1')
    sem_coord = base.loc[base['latitude'].isna(), 'NM_MUNICIPIO'].tolist()
    assert not sem_coord, f'municípios sem coordenada: {sem_coord}'
    base['DIST_CUIABA_KM'] = distancia_km(base['latitude'], base['longitude'])
    base = base.rename(columns={'latitude': 'LATITUDE', 'longitude': 'LONGITUDE'}).drop(columns=['CHAVE', 'APTOS_2022'])

    colunas = ['CD_MUNICIPIO', 'NM_MUNICIPIO', 'ELEITORADO_PERFIL', 'PCT_16_24', 'PCT_65_MAIS',
               'PCT_SUPERIOR_COMPLETO', 'LOG_ELEITORADO', 'ABST_2022_PCT', 'CRESC_ELEITORADO_PCT',
               'DIST_CUIABA_KM', 'LATITUDE', 'LONGITUDE', 'QT_APTOS', 'QT_ABSTENCOES', 'ABSTENCAO_PCT']
    return base[colunas].sort_values('CD_MUNICIPIO').reset_index(drop=True)


def checar(base):
    """Regras do negócio em código: se uma falhar, o ETL para."""
    assert base['CD_MUNICIPIO'].is_unique, 'município repetido'
    assert base['ABSTENCAO_PCT'].between(0, 100).all() and base['ABST_2022_PCT'].between(0, 100).all()
    assert (base['QT_ABSTENCOES'] <= base['QT_APTOS']).all()
    assert base.isna().sum().sum() == 0, 'há valores ausentes'
    assert base['DIST_CUIABA_KM'].between(0, 1500).all(), 'distância fora de MT'


def executar(saida='dados/base_analitica.csv', fontes=None, url_coordenadas=URL_COORDENADAS):
    fontes = fontes or {k: v[0] for k, v in FONTES.items()}
    print('lendo as fontes do TSE (só o trecho de MT de cada ZIP)...')
    perfil = ler_csv_do_zip(fontes['perfil_2026'], FONTES['perfil_2026'][1],
                            ['CD_MUNICIPIO', 'NM_MUNICIPIO', 'CD_FAIXA_ETARIA', 'CD_GRAU_ESCOLARIDADE', 'QT_ELEITORES'])
    cols_res = ['SG_UF', 'CD_MUNICIPIO', 'NR_TURNO', 'CD_CARGO', 'QT_APTOS', 'QT_ABSTENCOES']
    res_2026 = ler_csv_do_zip(fontes['resultado_2026'], FONTES['resultado_2026'][1], cols_res)
    res_2022 = ler_csv_do_zip(fontes['resultado_2022'], FONTES['resultado_2022'][1], cols_res)
    coordenadas = pd.read_csv(url_coordenadas)

    base = montar_base(perfil, res_2026, res_2022, coordenadas)
    novos = base.loc[base['ABST_2022_PCT'].isna(), 'NM_MUNICIPIO'].tolist()
    print('Municípios sem resultado em 2022 (instalados depois), retirados da base:', novos)
    base = base.dropna(subset=['ABST_2022_PCT']).reset_index(drop=True)
    checar(base)
    Path(saida).parent.mkdir(parents=True, exist_ok=True)
    base.to_csv(saida, index=False)
    print(f'{len(base)} municípios salvos em {saida}')
    return base


if __name__ == '__main__':
    executar()

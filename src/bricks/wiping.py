from typing import Dict
import pandas as pd
import numpy as np
from ..config.config import config


def wiping(df):

    app_config = config()

    name_coll_index = app_config['COLUMNS']['NAME_COLL_INDEX']

    name_coll_publications = app_config['COLUMNS']['NAME_COLL_PUBLICATIONS']
    name_coll_videos = app_config['COLUMNS']['NAME_COLL_VIDEOS']
    name_coll_hours = app_config['COLUMNS']["NAME_COLL_HOURS"]
    name_coll_revisited = app_config['COLUMNS']["NAME_COLL_REVISITED"]
    name_coll_studies = app_config['COLUMNS']["NAME_COLL_STUDIES"]

    # Deixando iniciais maiúsculas
    df[name_coll_index] = pd.Series(
        map(lambda x: x.title(), df[name_coll_index]), name=name_coll_index
    )

    # Ordenando as Coluna Nome
    df = df.sort_values(by=name_coll_index)

    # Alterando os espaços em branco por NaN
    df = df.apply(lambda data: data.replace("", np.nan))

    df = df.dropna(subset=[name_coll_index])

    # Tornando NaN em zero
    values = dict()

    values[name_coll_publications] = 0
    values[name_coll_videos] = 0
    values[name_coll_hours] = 0
    values[name_coll_revisited] = 0
    values[name_coll_studies] = 0

    df = df.fillna(values)

    # Tornando a coluna Nome como index
    df = df.set_index(name_coll_index)

    # Convertendo colunas para Float64
    df[name_coll_publications] = df[name_coll_publications].astype("float64")
    df[name_coll_videos] = df[name_coll_videos].astype("float64")
    df[name_coll_hours] = df[name_coll_hours].astype("float64")
    df[name_coll_revisited] = df[name_coll_revisited].astype("float64")
    df[name_coll_studies] = df[name_coll_studies].astype("float64")

    return df

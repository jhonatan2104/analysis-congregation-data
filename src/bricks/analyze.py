import pandas as pd
from ..config.config import config


def analyze_main(df, config):

    name_coll_service = config['COLUMNS']['NAME_COLL_SERVICE']
    name_coll_ministerial = config['COLUMNS']['NAME_COLL_MINISTERIAL']

    # Contando os Servos
    count_server = df[df[name_coll_service] ==
                      "Servo"].loc[:, name_coll_service].count()
    # Contando os Anciãos
    count_elder = df[df[name_coll_service] ==
                     "Ancião"].loc[:, name_coll_service].count()
    # Contando os Publicadores
    count_public = df[name_coll_ministerial].count()
    # Contando os Pioneiros Regular
    count_regular_pioneer = df[df[name_coll_ministerial] ==
                               "Pioneiro Regular"].loc[:, name_coll_ministerial].count()
    # Contando os Pioneiros Auxiliar
    count_auxiliary_pioneer = df[df[name_coll_ministerial] ==
                                 "Pioneiro Auxiliar"].loc[:, name_coll_ministerial].count()

    data = pd.DataFrame(
        [
            count_elder,
            count_server,
            count_regular_pioneer,
            count_auxiliary_pioneer,
            count_public
        ],
        index=["Ancião", "Servos", "Pioneiros Regulares",
               "Pioneiros Auxiliares", "Publicadores"],
        columns=["Total"]
    )

    return data


def getter_regular_pioneer(df, config):

    name_coll_ministerial = config['COLUMNS']['NAME_COLL_MINISTERIAL']

    data_regular_pioneer = df[df[name_coll_ministerial] == "Pioneiro Regular"]

    return data_regular_pioneer


def getter_auxiliary_pioneer(df, config):

    name_coll_ministerial = config['COLUMNS']['NAME_COLL_MINISTERIAL']

    data_auxiliary_pioneer = df[df[name_coll_ministerial]
                                == "Pioneiro Auxiliar"]

    return data_auxiliary_pioneer


def getter_publishers(df, config):

    name_coll_ministerial = config['COLUMNS']['NAME_COLL_MINISTERIAL']

    data_publishers = df[df[name_coll_ministerial] == "Publicador"]

    return data_publishers


def analyze_hours(df, regular_pioneer, auxiliary_pioneer, publishers, config):

    name_coll_publications = config['COLUMNS']['NAME_COLL_PUBLICATIONS']
    name_coll_videos = config['COLUMNS']['NAME_COLL_VIDEOS']
    name_coll_hours = config['COLUMNS']["NAME_COLL_HOURS"]
    name_coll_revisited = config['COLUMNS']["NAME_COLL_REVISITED"]
    name_coll_studies = config['COLUMNS']["NAME_COLL_STUDIES"]

    # Soma dos dados dos Pioneiros Regulares e Auxiliares e dos Publicadores
    df_total = pd.DataFrame(
        df.loc[:, name_coll_publications:name_coll_studies].sum(), columns=["Total"])
    sum_regular_pioneer = pd.DataFrame(
        regular_pioneer.loc[:, name_coll_publications:name_coll_studies].sum(), columns=["Pioneiros Regulares"])
    sum_auxiliary_pioneer = pd.DataFrame(
        auxiliary_pioneer.loc[:, name_coll_publications:name_coll_studies].sum(), columns=["Pioneiros Auxiliares"])
    sum_publishers = pd.DataFrame(
        publishers.loc[:, name_coll_publications:name_coll_studies].sum(), columns=["Publicadores"])
    df_geral = pd.concat(
        [sum_regular_pioneer, sum_auxiliary_pioneer, sum_publishers, df_total], axis=1)

    # Soma dos Pioneiros Regulares e Auxiliares e dos Publicadores que relataram
    regular_pioneer_reported = regular_pioneer[regular_pioneer[name_coll_hours] != 0].count()[
        name_coll_hours]
    auxiliary_pioneer_reported = auxiliary_pioneer[auxiliary_pioneer[name_coll_hours] != 0].count()[
        name_coll_hours]
    publishers_reported = publishers[publishers[name_coll_hours] != 0].count()[
        name_coll_hours]
    total_reported = df[df[name_coll_hours] != 0].count()[name_coll_hours]

    # Soma dos Pioneiros Regulares e Auxiliares e dos Publicadores que não relataram
    regular_pioneer_no_reported = regular_pioneer[regular_pioneer[name_coll_hours] == 0].count()[
        name_coll_hours]
    auxiliary_pioneer_no_reported = auxiliary_pioneer[auxiliary_pioneer[name_coll_hours] == 0].count()[
        name_coll_hours]
    publishers_no_reported = publishers[publishers[name_coll_hours] == 0].count()[
        name_coll_hours]
    total_no_reported = df[df[name_coll_hours] == 0].count()[name_coll_hours]

    ser = pd.Series([
        regular_pioneer_reported,
        auxiliary_pioneer_reported,
        publishers_reported,
        total_reported],
        index=['Pioneiros Regulares',
               'Pioneiros Auxiliares', 'Publicadores', 'Total'],
        name="Relataram"
    )
    ser_no = pd.Series([
        regular_pioneer_no_reported,
        auxiliary_pioneer_no_reported,
        publishers_no_reported,
        total_no_reported],
        index=['Pioneiros Regulares',
               'Pioneiros Auxiliares', 'Publicadores', 'Total'],
        name="Não Relataram"
    )
    df_geral = df_geral.append([ser, ser_no])

    return df_geral


def getter_not_reported(df):
    df_zero = df[df['Horas'] == 0]
    return df_zero


def getter_non_progressive_studies(df):
    df_p_sem_revisitas = df[(df['Estudos'] >= 1) & (
        df['Revisitas']/df['Estudos'] <= 2)]
    return df_p_sem_revisitas


def getter_brother_with_observation(df):
    df_obs = df[df['Obs'].notna()]
    return df_obs


def getter_without_studies(df):
    df_p_sem_estudos = df[(df['Estudos'] == 0)]
    return df_p_sem_estudos


def analyze(df):
    app_config = config()

    main = analyze_main(df, config=app_config)
    regular_pioneer = getter_regular_pioneer(df, config=app_config)
    auxiliary_pioneer = getter_auxiliary_pioneer(df, config=app_config)
    publishers = getter_publishers(df, config=app_config)
    df_geral = analyze_hours(df, regular_pioneer=regular_pioneer,
                             auxiliary_pioneer=auxiliary_pioneer,
                             publishers=publishers, config=app_config)

    not_reported = getter_not_reported(df)
    non_progressive_studies = getter_non_progressive_studies(df)
    brother_with_observation = getter_brother_with_observation(df)
    without_studies = getter_without_studies(df)

    data = dict()

    data[app_config['NAME_TABLE_GENERATE']['BASE']] = df

    data[app_config['NAME_TABLE_GENERATE']['MAIN']] = main

    data[app_config['NAME_TABLE_GENERATE']['REGULAR_PIONEER']] = regular_pioneer

    data[app_config['NAME_TABLE_GENERATE']
         ['AUXILIARY_PIONEER']] = auxiliary_pioneer

    data[app_config['NAME_TABLE_GENERATE']['PUBLISHERS']] = publishers

    data[app_config['NAME_TABLE_GENERATE']['HOURS']] = df_geral

    data[app_config['NAME_TABLE_GENERATE']['NOT_REPORTED']] = not_reported

    data[app_config['NAME_TABLE_GENERATE']
         ['NON_PROGRESSIVE_STUDIES']] = non_progressive_studies

    data[app_config['NAME_TABLE_GENERATE']
         ['BROTHER_WITH_OBSERVATION']] = brother_with_observation

    data[app_config['NAME_TABLE_GENERATE']
         ['BROTHER_WITHOUT_STUDIES']] = without_studies

    return data

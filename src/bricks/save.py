import pandas as pd
from ..config.config import config
from ..utils import get_data_now


def save(_dict):
    app_config = config()

    destination_folders = app_config['DESTINATION_FOLDER']

    date_now = get_data_now()

    years = date_now["years"]
    month = date_now["month"]

    name_df = app_config['NAME_TABLE_GENERATE']['BASE']
    name_main = app_config['NAME_TABLE_GENERATE']['MAIN']
    name_regular_pioneer = app_config['NAME_TABLE_GENERATE']['REGULAR_PIONEER']
    name_auxiliary_pioneer = app_config['NAME_TABLE_GENERATE']['AUXILIARY_PIONEER']
    name_publishers = app_config['NAME_TABLE_GENERATE']['PUBLISHERS']
    name_df_geral = app_config['NAME_TABLE_GENERATE']['HOURS']
    name_not_reported = app_config['NAME_TABLE_GENERATE']['NOT_REPORTED']
    name_non_progressive_studies = app_config['NAME_TABLE_GENERATE']['NON_PROGRESSIVE_STUDIES']
    name_brother_with_observation = app_config['NAME_TABLE_GENERATE']['BROTHER_WITH_OBSERVATION']
    name_without_studies = app_config['NAME_TABLE_GENERATE']['BROTHER_WITHOUT_STUDIES']

    df = _dict[name_df]
    main = _dict[name_main]
    regular_pioneer = _dict[name_regular_pioneer]
    auxiliary_pioneer = _dict[name_auxiliary_pioneer]
    publishers = _dict[name_publishers]
    df_geral = _dict[name_df_geral]

    not_reported = _dict[name_not_reported]
    non_progressive_studies = _dict[name_non_progressive_studies]
    brother_with_observation = _dict[name_brother_with_observation]
    without_studies = _dict[name_without_studies]

    path_doc = f'{destination_folders}/{years}-{month}.xlsx'

    with pd.ExcelWriter(path_doc) as writer:
        df_geral.to_excel(writer, sheet_name=name_df_geral)
        main.to_excel(writer, sheet_name=name_main)
        regular_pioneer.to_excel(writer, sheet_name=name_regular_pioneer)
        auxiliary_pioneer.to_excel(writer, sheet_name=name_auxiliary_pioneer)
        publishers.to_excel(writer, sheet_name=name_publishers)
        brother_with_observation.to_excel(
            writer, sheet_name=name_brother_with_observation)
        not_reported.to_excel(writer, sheet_name=name_not_reported)
        non_progressive_studies.to_excel(
            writer, sheet_name=name_non_progressive_studies)
        without_studies.to_excel(writer, sheet_name=name_without_studies)
        df.to_excel(writer, sheet_name=name_df)

    return path_doc

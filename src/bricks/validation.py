import sys
from ..config.config import config


def validation(df):

    app_config = config()

    destination_folder = app_config['DESTINATION_FOLDER']
    name_coll_service = app_config['COLUMNS']['NAME_COLL_SERVICE']
    name_coll_ministerial = app_config['COLUMNS']['NAME_COLL_MINISTERIAL']
    # Verificando Erro Nome repetido
    erro_name_repeated = df.index.value_counts()
    df_erro_name_repeated = df.loc[erro_name_repeated > 1, :]
    if len(df_erro_name_repeated) > 0:
        print("Erro: name repeated")
        df_erro_name_repeated.to_excel(
            f"{destination_folder}/NOME_REPETIDO.xlsx",
            sheet_name='Erro'
        )
        sys.exit()

    # Verificando Erros coluna Privilégio de serviço
    erro_col_service_privilege = df[
        (df[name_coll_service].notna()) &
        (~df[name_coll_service].isin(app_config["ENUM_COLL_SERVICE"]))
    ]
    if len(erro_col_service_privilege) > 0:
        print("Erro: column service privilege")
        erro_col_service_privilege.to_excel(
            f"{destination_folder}/DADOS_INVÁLIDOS_PRIVILÉGIOS_SERVICO.xlsx",
            sheet_name='Erro'
        )
        sys.exit()

    # Verificando Erros coluna Privilégio ministerial
    erro_col_service_ministerial = df[
        (~df[name_coll_ministerial].isin(app_config["ENUM_COLL_MINISTERIAL"]))
    ]
    if len(erro_col_service_ministerial) > 0:
        print("Erro: column service ministerial")
        erro_col_service_ministerial.to_excel(
            f"{destination_folder}/DADOS_INVÁLIDOS_PRIVILÉGIOS_MINISTERIAL.xlsx",
            sheet_name='Erro')
        sys.exit()

    return df

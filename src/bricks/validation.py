import sys
from ..config.config import config
from ..bricks.mail import message


def validation(df):

    app_config = config()

    # Config message erro
    name_congregation = app_config['NAME_CONGREGATION']
    name_sheet = f'Erro-{name_congregation}'
    body = 'Estamos enviando em anexo a planilia em um formato que te ajude a encontrar o erro'

    destination_folder = app_config['DESTINATION_FOLDER']
    name_coll_service = app_config['COLUMNS']['NAME_COLL_SERVICE']
    name_coll_ministerial = app_config['COLUMNS']['NAME_COLL_MINISTERIAL']
    # Verificando Erro Nome repetido
    erro_name_repeated = df.index.value_counts()
    df_erro_name_repeated = df.loc[erro_name_repeated > 1, :]
    if len(df_erro_name_repeated) > 0:
        print("Erro: name repeated")

        path_doc = f"{destination_folder}/NOME_REPETIDO.xlsx"

        subject = 'Algo deu errado: Existe nomes repetidos na sua planilia'

        df_erro_name_repeated.to_excel(
            path_doc,
            sheet_name='Erro'
        )

        message(
            path_doc,
            body,
            subject,
            name_sheet
        )
        sys.exit()

    # Verificando Erros coluna Privilégio de serviço
    erro_col_service_privilege = df[
        (df[name_coll_service].notna()) &
        (~df[name_coll_service].isin(app_config["ENUM_COLL_SERVICE"]))
    ]
    if len(erro_col_service_privilege) > 0:
        print("Erro: column service privilege")

        path_doc = f"{destination_folder}/DADOS_INVÁLIDOS_PRIVILÉGIOS_SERVICO.xlsx"
        subject = f'Algo deu errado: Tipos inválido de {name_coll_service}'

        erro_col_service_privilege.to_excel(
            f"{destination_folder}/DADOS_INVÁLIDOS_PRIVILÉGIOS_SERVICO.xlsx",
            sheet_name='Erro'
        )

        message(
            path_doc,
            body,
            subject,
            name_sheet
        )

        sys.exit()

    # Verificando Erros coluna Privilégio ministerial
    erro_col_service_ministerial = df[
        (~df[name_coll_ministerial].isin(app_config["ENUM_COLL_MINISTERIAL"]))
    ]
    if len(erro_col_service_ministerial) > 0:
        print("Erro: column service ministerial")

        path_doc = f"{destination_folder}/DADOS_INVÁLIDOS_PRIVILÉGIOS_MINISTERIAL.xlsx"
        subject = f'Algo deu errado: Tipos inválido de {name_coll_ministerial}'

        erro_col_service_ministerial.to_excel(
            f"{destination_folder}/DADOS_INVÁLIDOS_PRIVILÉGIOS_MINISTERIAL.xlsx",
            sheet_name='Erro')

        message(
            path_doc,
            body,
            subject,
            name_sheet
        )

        sys.exit()

    return df

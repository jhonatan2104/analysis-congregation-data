import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from ..config.config import config


def getting():

    app_config = config()

    file_credentials = app_config['FILE_GOOGLE']
    name_sheet1_google = app_config['NAME_SHEET']
    # Adicionando as credenciais, e o escopo da pesquisa
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        file_credentials, scope)
    gc = gspread.authorize(credentials)

    # Abrindo o folha do Google
    wks = gc.open(name_sheet1_google).sheet1

    # Lendo no formato de várias listas
    data = wks.get_all_values()

    # Definindo dados e cabeçalho
    columns = data[0]
    values = data[1:]

    # Criando dataframe
    df = pd.DataFrame(values, columns=columns)

    return df

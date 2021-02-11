
import json

FILE_CONFIG = 'src/config/config-prod.json'


def config():
    with open(FILE_CONFIG) as f:
        data = json.load(f)

    return data

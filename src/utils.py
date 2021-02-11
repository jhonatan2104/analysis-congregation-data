from datetime import datetime


def get_data_now():
    now = datetime.now()
    years = now.year
    month = now.month-1

    d = dict()

    d["now"] = now
    d["years"] = years
    d["month"] = month

    return d

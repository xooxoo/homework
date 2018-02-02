from datetime import datetime


def get_days_to_new_year():
    c = int(datetime.toordinal(datetime(datetime.now().year + 1, 1, 1)) - datetime.toordinal(datetime.today()))
    return c


from datetime import date, datetime, timedelta


def get_str_today(format="%Y-%m-%d"):
    return date.today().strftime(format)


def get_str_now(format="%Y-%m-%d %H:%M:%S"):
    return datetime.now().strftime(format)


def get_weekday(in_date=None):
    if in_date is None:
        in_date = date.today()
    return in_date.weekday()


def get_str_date(in_date=None, format="%Y-%m-%d"):
    if in_date is None:
        in_date = date.today()
    return in_date.strftime(format)


def get_str_datetime(in_datetime=None, format="%Y-%m-%d %H:%M:%S"):
    if in_datetime is None:
        in_datetime = datetime.now
    return in_datetime.strftime(format)


def get_datetime(str_datetime, format="%Y-%m-%d %H:%M:%S"):
    return datetime.strptime(str_datetime, format)


def get_days_by_date(begin_date, end_date):
    begin_datetime = datetime(begin_date.year, begin_date.month, begin_date.day)
    end_datetime = datetime(end_date.year, end_date.month, end_date.day)
    return (end_datetime - begin_datetime).days


def get_days_by_datetime(begin_datetime, end_datetime):
    return (end_datetime - begin_datetime).days


def get_seconds_by_datetime(begin_datetime, end_datetime):
    return (end_datetime - begin_datetime).seconds


def get_minutes_by_datetime(begin_datetime, end_datetime):
    return (end_datetime - begin_datetime).minutes


def get_datetime_by_delta(in_datetime=None, kwargs=None):
    # days, seconds, microseconds, milliseconds, minutes, weeks
    if in_datetime is None:
        in_datetime = datetime.now()
    return in_datetime + timedelta(kwargs)

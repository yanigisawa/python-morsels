from datetime import datetime, timedelta
from fractions import Fraction

SECONDS_PER_YEAR = 365.2425 * 24 * 60 * 60


def is_over(age, date_str):
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    years = timedelta(seconds=SECONDS_PER_YEAR * age)
    return (datetime.now() - dt) > years


def yearsago(years, from_date=None):
    if from_date is None:
        from_date = datetime.now()
    try:
        return from_date.replace(year=from_date.year - years)
    except ValueError:
        # Must be 2/29!
        assert from_date.month == 2 and from_date.day == 29  # can be removed
        return from_date.replace(month=2, day=28, year=from_date.year - years)


from datetime import date


def get_age(date_str, exact=False):
    if exact:
        return get_age_exact(date_str)
    born = datetime.strptime(date_str, "%Y-%m-%d")
    today = date.today()
    today_tup = (today.month, today.day)
    born_tup = (born.month, born.day)
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def get_age_exact(date_str):
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    today = date.today()
    diff = datetime.now() - dt
    other_diff = dt.timestamp() - datetime.now().timestamp()
    years = int(diff.total_seconds() / (SECONDS_PER_YEAR))
    year_days = 366 if today.year % 4 == 0 else 365
    other_year_days = 366 if dt.year % 4 == 0 else 365
    days_till_eoy = other_year_days - dt.timetuple().tm_yday
    days = today.timetuple().tm_yday + days_till_eoy

    return years + Fraction(days, year_days)

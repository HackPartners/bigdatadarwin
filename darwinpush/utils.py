import pytz
from datetime import datetime, timedelta

def timezone_for_date_and_time(d, t):
    tz = pytz.timezone("Europe/London")
    dt = pytz.utc.localize(datetime.combine(d, t))
    if dt.astimezone(tz).utcoffset().seconds / 3600 == 1:
        return pytz.timezone("Etc/GMT+1")
    else:
        return pytz.timezone("Etc/GMT")



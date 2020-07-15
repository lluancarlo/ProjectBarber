from datetime import datetime

from iso8601 import iso8601
from pytz import UTC

UTC_FORMAT = '%Y-%m-%dT%H:%M:%S.00Z'


def localize(value):
    return UTC.localize(value)


def now():
    return localize(datetime.now())


def now_to_string():
    return now().strftime(UTC_FORMAT)


def stringutc_to_datetime(value):
    return iso8601.parse_date(value, UTC)
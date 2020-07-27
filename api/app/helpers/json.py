import re
from datetime import datetime
from json import dumps

from flask.json import JSONEncoder, JSONDecoder

from .datetime_helpers import stringutc_to_datetime

remove_keys_json = ["secret", "id"]


def json_decoder_handler(obj):
    return obj


def json_encoder_handler(obj):
    if hasattr(obj, "json") and callable(getattr(obj, "json")):
        return obj.json()
    if hasattr(obj, "isoformat") and callable(getattr(obj, "isoformat")):
        return obj.isoformat() + "Z"
    elif hasattr(obj, "__str__") and callable(getattr(obj, "__str__")):
        return str(obj)
    else:
        print("obj:", obj)
        raise TypeError(obj)


def json_dumps(value: dict):
    return value


class ModifyJSONEncoder(JSONEncoder):
    def default(self, o):
        return json_dumps(o)

    def encode(self, o):
        return self.default(o)


class ModifyJSONDecoder(JSONDecoder):
    def decoder(self, d):
        return json_decoder_handler(d)


def sanetize_request(values):
    if not values:
        return values
    if isinstance(values, dict):
        for key in values.keys():
            values[key] = sanetize_request(values[key])
        return values
    if isinstance(values, list):
        for key, item in enumerate(values):
            values[key] = sanetize_request(item)
        return values
    if not isinstance(values, str):
        return values
    if re.match('^[0-9]{4}[-/][0-9]{2}[-/]$', values):
        values = datetime.strptime(values, "%Y-%m-%d")
        return values
    if re.match('^[0-9]{4}[-/][0-9]{2}[-/][0-9]{2}T.*$', values):
        values = stringutc_to_datetime(values)
        return values

    return values


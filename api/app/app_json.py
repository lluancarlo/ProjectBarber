from flask import Blueprint, Flask

from .helpers.json import ModifyJSONEncoder, ModifyJSONDecoder


class AppBlueprint(Blueprint):
    json_encoder = ModifyJSONEncoder
    json_decoder = ModifyJSONDecoder
    pass

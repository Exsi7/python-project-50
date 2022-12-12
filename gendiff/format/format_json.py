import json


def format_json(value):
    return str(json.dumps(value, sort_keys=True))

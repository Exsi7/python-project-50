import json


def format_json(value):
    return json.dumps(value, sort_keys=True)

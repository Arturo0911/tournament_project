import json

def decode_json(argument):


    json_decoder = argument.decode('utf-8')
    body = json.loads(json_decoder)
    return body
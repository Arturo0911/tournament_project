import json

def decode_raw_data_post_method(data_to_parse):

    json_unicode = data_to_parse.decode('utf-8')
    body = json.loads(json_unicode)
    return body
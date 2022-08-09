import ast
import json
from TokenList.models import TokenModel
JSON_FILE_PATH = "tokenList.json"


def load_json():

    with open(JSON_FILE_PATH, 'r') as jf:
        json_dict = json.load(jf)

    return json_dict

def format_json():
    '''Reads the json file and save it on the temp_file.json
    '''
    json_file = load_json()
    key_list = list(json_file.keys())
    total_files = []
    for key in key_list:
        dict_file = json_file[key]
        for file in dict_file:
            new_file = file.copy()
            new_file['channel_id'] = key
            total_files.append(new_file)
    # Uploads the file
    TokenModel.objects.bulk_create([TokenModel(**file) for file in total_files])

def update_json():
    get_all_objects = TokenModel.objects.all().values()
    json_dict = dict()
    for object_file in get_all_objects:
        channel_id = object_file['channel_id']
        if channel_id not in json_dict:
            json_dict[channel_id] = []
    
        # deleting not required file
        object_file.pop('id')
        object_file.pop('channel_id')
        new_json = {x:y for x,y in object_file.items() if y is not None}
        if new_json.get('pairs'):
            new_json['pairs'] = ast.literal_eval(new_json['pairs'])
        json_dict[channel_id].append(new_json)
    return json_dict

def write_json():
    json_dict = update_json()
    with open('test.json', 'w') as jf:
        json.dump(json_dict, jf, indent=4)




if __name__ == '__main__':
    format_json()
    breakpoint()
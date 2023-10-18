from sys import argv
import json, markdown_to_json, pathlib, os
home_dir = (pathlib.Path.home())

path = f'{home_dir}/.config/YourCheatSheet.md'
file = pathlib.Path(path)

content = file.read_text()

json_string = markdown_to_json.jsonify(content)
json_object = json.loads(json_string)


def key_search(key, json):
    results = []
    
    if isinstance(json, dict):
        if key in json:
            keysList = json[key]
            if isinstance(keysList, dict):
                for i in keysList.keys():
                    results.append(i)
            else:
                results.append(keysList)
        for k, v in json.items():
            results.extend(key_search(key, v))
    elif isinstance(json, list):
        for item in json:
            results.extend(key_search(key, item))
    
    return results

search_results = key_search('Pytest', json_object)
for result in search_results:
    print(result)




#!/usr/bin/env python3
import markdown_to_json, pathlib, json 
from sys import argv
from main import Parser

path_str = argv[1]
path = pathlib.Path(path_str)
content = path.read_text()
json_string = markdown_to_json.jsonify(content)
json_object = json.loads(json_string)
# print(json_object)

docs = Parser(json_object)
docs.main()



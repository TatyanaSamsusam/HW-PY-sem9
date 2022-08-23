
import json
from typing import Dict

def read_from_file():
    with open ('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data

def write_to_file(data):
    with open ('data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent = 4)





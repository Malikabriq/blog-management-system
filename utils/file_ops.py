import json
import os

def read_json(path: str):
    if not os.path.exists(path):
        return None
    with open(path, "r") as f:
        return json.load(f)

def write_json(path: str, data: dict):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def delete_file(path: str):
    if os.path.exists(path):
        os.remove(path)

import json
path="data/sample.json"


with open(path) as file:
    data=json.load(file)

def entities():
    return len(data)

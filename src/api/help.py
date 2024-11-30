import json

# path to json file
CVE_JSON = "<YOUR_PATH>"

def read_json() -> dict:
    """converts json to dictionary"""
    with open(CVE_JSON, "r") as file:
        return json.load(file)

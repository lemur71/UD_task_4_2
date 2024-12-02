import json
from migration.create_cve_index import client, save_index_name

# path to json file
CVE_JSON = "C:\\Users\\1\\Desktop\\UD\\4 PYTHON\\task4_2\\known_exploited_vulnerabilities.json"

def read_json() -> dict:
    """converts json to dictionary"""
    with open(CVE_JSON, "r") as file:
        return json.load(file)
    
def save_report(report_data: list):
    """save the report data to elasticsearch"""
    client.index(index=save_index_name, document={"reports": report_data})

from elasticsearch import Elasticsearch
from fastapi import APIRouter

ELASTIC_URL = "<YOUR_ELASTIC_URL>"
ELASTIC_API_ENCODED = "<YOUR_ELASTIC_KEY>"
index_name = "<YOUR_ELASTIC_DATA_INDEX_NAME>"
save_index_name = "<YOUR_ELASTIC_REPORTS_INDEX_NAME>"

router = APIRouter(tags=["Create new index in Elastic Search"])

@router.get("/create/index")
def get_new():
    return create_cve_index()

client = Elasticsearch(
    ELASTIC_URL,
    api_key=ELASTIC_API_ENCODED
)

def create_cve_index():
    response = client.indices.create(index=index_name)
    response_save = client.indices.create(index=save_index_name)
    
    if response.meta.status == 200 and response_save.meta.status == 200:
        return "Success"
    else:
        return "Creation Failed"

if __name__ == "__main__":
    create_cve_index()
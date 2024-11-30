from elasticsearch import Elasticsearch
from fastapi import APIRouter

ELASTIC_URL = "<YOUR_ELASTICSEARCH_URL>"
ELASTIC_API_ENCODED = "<YOUR_ELASTICSEARCH_ENCODED_API>"
index_name = "<INDEX_NAME>"

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
    if response.meta.status == 200:
        return "Success"
    else:
        return "Creation Failed"

if __name__ == "__main__":
    create_cve_index()
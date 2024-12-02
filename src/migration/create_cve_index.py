from elasticsearch import Elasticsearch
from fastapi import APIRouter

ELASTIC_URL = "https://87ff060a920046c783627169d2b69e54.us-central1.gcp.cloud.es.io:443"
ELASTIC_API_ENCODED = "SFZPY2lKTUJkY0FDN0pDTkh5MS06UDBYTTJzSlZTX1daOHRqQ2ZFTS1rdw=="
index_name = "info_index"
save_index_name = "save_index"

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
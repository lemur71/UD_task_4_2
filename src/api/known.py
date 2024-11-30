from api.help import read_json
from fastapi import APIRouter
from migration.create_cve_index import client, index_name

router = APIRouter(tags=["Known Ransomware Campain Use (max 10)"])

@router.get("/get/known")
def get_known():
    return get_known_cve(10)

def get_known_cve(max_quantity: int) -> list:
    """retun CVEs that is in ransomware campain use"""
    result = []
    response = client.search(
        index=index_name,
        body={
            "size": max_quantity,
            "query": {
                "bool": {
                    "must": [
                        {"match":{"cve.knownRansomwareCampaignUse.keyword": "Known"}}
                    ]
                }
            }
        } 
    )
    result = [hit["_source"] for hit in response["hits"]["hits"]]
    return result
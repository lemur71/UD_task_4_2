from fastapi import APIRouter
from api.help import save_report
from migration.create_cve_index import client, index_name, save_index_name

router = APIRouter(tags=["10 newest CVEs"])

@router.get("/get/new")
def get_new():
    return get_n_new_cves(10)

def get_n_new_cves(quantity: int) -> list:
    """retun list of N newest CVEs"""
    result = []
    response = client.search(
        index=index_name,
        body={
            "size": quantity,
            "sort": [
                {"cve.dateAdded": {"order": "desc"}}
            ],
            "query": {
                "match_all": {}
            }
        }
    )
    result = [hit["_source"] for hit in response["hits"]["hits"]]
    save_report(result)
    return result

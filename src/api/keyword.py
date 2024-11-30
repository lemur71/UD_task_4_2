from api.help import read_json
from fastapi import APIRouter
import re
from migration.create_cve_index import client, index_name

router = APIRouter(tags=["Search by keyword"])

@router.get("/get")
def get_keyword(query: str):
    return find_keyword(query)

def find_keyword(keyword: str) -> list:
    """return all CVEs where keyword was found"""
    result = []
    response = client.search(
        index=index_name,
        body={
            "query": {
                "bool": {
                    "must": {
                        "multi_match": {
                            "query": keyword,
                            "fields": ["cve.vendorProject",
                                        "cve.product",
                                        "cve.vulnerabilityName",
                                        "cve.shortDescription",
                                        "cve.requiredAction",
                                        "cve.notes"]
                        }
                    }
                } 
            }
        }
    )

    result = [hit["_source"] for hit in response["hits"]["hits"]]
    return result

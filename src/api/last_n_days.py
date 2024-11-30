from api.help import read_json
from datetime import date, datetime, timedelta
from fastapi import APIRouter
from elasticsearch import Elasticsearch
from migration.create_cve_index import client, index_name, ELASTIC_URL

router = APIRouter(tags=["CVEs for past 5 days (max 40 CVEs)"])

@router.get("/get/all")
def get_all():
    return get_recent_cves(5, 40)

def get_recent_cves(days: int, max_quantity: int) -> list:
    """retun list of CVEs added last N days"""
    def n_days_ago(days_ago: int) -> str:
        """calculate date for N days ago"""
        return date.today() - timedelta(days=days_ago)

    
    response = client.search(index=index_name, body={
        "size": max_quantity,
        "query": {
            "range": {
                "cve.dateAdded": {
                    "gte": n_days_ago(days)
                }
            }
        }
    })

    result = [hit["_source"] for hit in response["hits"]["hits"]]
    return result

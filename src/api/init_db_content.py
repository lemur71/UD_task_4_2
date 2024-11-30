from api.help import read_json
from fastapi import APIRouter
from elasticsearch import Elasticsearch
from uuid import uuid4
from migration.create_cve_index import client, index_name

router = APIRouter(tags=["Initialize data "])


@router.get("/init-db")
def text_init_db_content():
    content = read_json()
    for cve in content["vulnerabilities"]:
        doc = {
            "cve":cve
        }
        client.create(index=index_name,id=str(uuid4()), body=doc)
    return "Init success"

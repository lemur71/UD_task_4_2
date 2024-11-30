from fastapi import APIRouter

router = APIRouter(tags=["Info page"])

@router.get("/info")
def get_info():
    return info

info = {
    "author_info" : {
        "author_name": "Mykola",
        "author_surname": "Savitskyi",
    },
    "app_info": {
    "app_description": "This is API task from UnderDefense #4",
    "option1": "/get/all -- returns all CVEs for past 5 days (max 40 CVEs)",
    "option2": "/get/new -- returns 10 newest CVEs",
    "option3": "/get/known -- returns CVEs were knownRansomwareCampaignUse - Known (max 10 CVEs)",
    "option4": "/get?query='key' -- returns CVEs that contain keyword",
    },
}

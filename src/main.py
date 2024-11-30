from fastapi import FastAPI
from api import info, last_n_days, new_n, known, keyword, init_db_content
from migration import create_cve_index

app = FastAPI()

app.include_router(info.router)
app.include_router(last_n_days.router)
app.include_router(new_n.router)
app.include_router(known.router)
app.include_router(keyword.router)
app.include_router(init_db_content.router)
app.include_router(create_cve_index.router)

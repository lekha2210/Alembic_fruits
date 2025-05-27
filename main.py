from fastapi import FastAPI
from core.db import create_db_and_tables
from routes.logins import router as login_router

app = FastAPI()

app.include_router(login_router, prefix="/api")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
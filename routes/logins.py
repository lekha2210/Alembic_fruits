from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.db import get_db
from schemas.logins import LoginCreate, LoginMessageResponse
from crud.logins import get_login, create_login

router = APIRouter()

@router.get("/login", response_model=LoginMessageResponse)
async def login(username: str, password: str, db: Session = Depends(get_db)):
    db_login = get_login(db, username=username)
    if not db_login or db_login.password != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    return {
        "message": "Login successful",
        "login": db_login
    }

@router.post("/create_login", response_model=LoginMessageResponse)
async def create_login_route(login: LoginCreate, db: Session = Depends(get_db)):
    existing_login = get_login(db, username=login.username)
    if existing_login:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    db_login = create_login(db, login=login)
    return {
        "message": "Login created successfully",
        "login": db_login
    }
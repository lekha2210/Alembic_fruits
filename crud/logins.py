from sqlalchemy.orm import Session
from models.login import Login
from schemas.logins import LoginCreate

def get_login(db: Session, username: str):
    return db.query(Login).filter(Login.username == username).first()

def create_login(db: Session, login: LoginCreate):
    db_login = Login(username=login.username, password=login.password)
    db.add(db_login)
    db.commit()
    db.refresh(db_login)
    return db_login
from schemas import *
from models import User

def create_user(db, user:UserCreate):
    db_user = User(username= user.usename, email= user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db, user_id:int):
    return db.query(User).filter(User.id == user.id).first

def get_all_users(db):
    return db.query(User).all()
from sqlalchemy.orm import Session
from model import User
# from schema import UserSchema

def db_register_user(db: Session, username, password):
    db_user = User(username=username, password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
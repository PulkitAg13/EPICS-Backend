from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import User
from schemas import UserCreate, UserLogin
from auth import hash_pw, verify_pw
from utils.jwt_handler import create_token

router = APIRouter(prefix="/auth")

@router.post("/signup")
def signup(data: UserCreate, db: Session = Depends(get_db)):
    user = User(name=data.name, phone=data.phone, password_hash=hash_pw(data.password))
    db.add(user)
    db.commit()
    return {"msg": "Signup successful"}

@router.post("/login")
def login(data: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.phone == data.phone).first()
    if not user or not verify_pw(data.password, user.password_hash):
        raise HTTPException(401, "Invalid credentials")

    token = create_token({"user_id": user.id})
    return {"access_token": token}

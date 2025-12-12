from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import StockListing

router = APIRouter(prefix="/stock")

@router.post("")
def create_stock(crop: str, qty: float, db: Session = Depends(get_db)):
    s = StockListing(user_id="dummy", crop=crop, quantity=qty)
    db.add(s)
    db.commit()
    return {"msg": "Stock added"}

@router.get("/my")
def my_stock(db: Session = Depends(get_db)):
    return db.query(StockListing).all()

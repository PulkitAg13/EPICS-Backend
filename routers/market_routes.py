from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import MarketRecord

router = APIRouter(prefix="/market")

@router.get("/current")
def current_prices(crop: str, district: str, db: Session = Depends(get_db)):
    rec = db.query(MarketRecord).filter_by(crop=crop, district=district).all()
    return rec

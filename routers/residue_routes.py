from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import ResidueRequest

router = APIRouter(prefix="/residue")

@router.post("/request")
def create_residue(crop_type: str, qty: float, village: str, db: Session = Depends(get_db)):
    r = ResidueRequest(
        user_id="dummy",
        crop_type=crop_type,
        residue_qty=qty,
        village=village,
        status="Pending"
    )
    db.add(r)
    db.commit()
    return {"msg": "Residue request added"}

@router.get("/my-requests")
def my_residue(db: Session = Depends(get_db)):
    return db.query(ResidueRequest).all()

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import DiseaseCase
from schemas import DiseaseInput

router = APIRouter(prefix="/disease")

@router.post("/case")
def create_case(data: DiseaseInput, db: Session = Depends(get_db)):
    case = DiseaseCase(
        user_id="dummy",
        crop_type=data.crop_type,
        image_url=data.image_url,
        model_prediction="Blight",
        confidence=0.92,
        disease_label="Leaf Blight"
    )
    db.add(case)
    db.commit()
    return {"prediction": case.model_prediction, "confidence": case.confidence}

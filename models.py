from sqlalchemy import Column, String, Integer, Float, Date, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from database import Base

def uid():
    return str(uuid.uuid4())

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, default=uid)
    name = Column(String)
    phone = Column(String, unique=True)
    password_hash = Column(String)

class Field(Base):
    __tablename__ = "fields"
    id = Column(String, primary_key=True, default=uid)
    user_id = Column(String, ForeignKey("users.id"))
    land_area = Column(Float)
    soil_type = Column(String)

class DiseaseCase(Base):
    __tablename__ = "disease_cases"
    id = Column(String, primary_key=True, default=uid)
    user_id = Column(String, ForeignKey("users.id"))
    crop_type = Column(String)
    image_url = Column(String)
    model_prediction = Column(String)
    confidence = Column(Float)
    disease_label = Column(String)

class Recommendation(Base):
    __tablename__ = "recommendations"
    id = Column(String, primary_key=True, default=uid)
    disease_label = Column(String)
    crop_type = Column(String)
    pesticide_name = Column(String)
    fertilizer_name = Column(String)
    instructions_text = Column(String)

class MarketRecord(Base):
    __tablename__ = "market_records"
    id = Column(String, primary_key=True, default=uid)
    crop = Column(String)
    district = Column(String)
    price_per_quintal = Column(Float)

class StockListing(Base):
    __tablename__ = "stock_listings"
    id = Column(String, primary_key=True, default=uid)
    user_id = Column(String)
    crop = Column(String)
    quantity = Column(Float)

class ResidueRequest(Base):
    __tablename__ = "residue_requests"
    id = Column(String, primary_key=True, default=uid)
    user_id = Column(String)
    crop_type = Column(String)
    residue_qty = Column(Float)
    village = Column(String)
    status = Column(String)

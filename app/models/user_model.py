# app/models/user_model.py

from sqlalchemy import Column, DateTime, Integer, String, Text
from app.database import Base
from datetime import datetime


# ✅ USER TABLE (ONLY ONE TIME DEFINE)
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100), unique=True, index=True)
    password = Column(String(200))
    otp_expiry = Column(DateTime, nullable=True) 
    otp = Column(String(10), nullable=True)   # ✅ OTP FIX


# ✅ PREDICTION TABLE
class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    user_email = Column(String(100))
    skills = Column(Text)
    prediction = Column(String(100))
    

profile_pic = Column(String, nullable=True)
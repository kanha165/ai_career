from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.user_model import User
from app.schemas.user_schema import UserSignup, UserLogin, ResetPasswordSchema
from app.utils.hashing import hash_password, verify_password
from app.utils.token import create_token
from app.database import SessionLocal
from app.utils.email_service import send_otp_email
from app.config import GOOGLE_CLIENT_ID

from google.oauth2 import id_token
from google.auth.transport import requests

import random
from datetime import datetime, timedelta

router = APIRouter()


# =========================
# 🔥 DB Dependency
# =========================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# =========================
# ✅ SIGNUP
# =========================
@router.post("/signup")
def signup(user: UserSignup, db: Session = Depends(get_db)):

    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already exists")

    new_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User created successfully"}


# =========================
# ✅ LOGIN
# =========================
@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user:
        raise HTTPException(status_code=400, detail="User not found")

    if not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid password")

    token = create_token({"email": db_user.email})

    return {
        "access_token": token,
        "token_type": "bearer"
    }


# =========================
# ✅ GOOGLE LOGIN
# =========================
@router.post("/google")
def google_login(token: str):
    try:
        idinfo = id_token.verify_oauth2_token(
            token,
            requests.Request(),
            GOOGLE_CLIENT_ID   # ✅ env se aa raha hai
        )

        email = idinfo.get("email")

        if not email:
            raise HTTPException(status_code=400, detail="Email not found in Google token")

        jwt_token = create_token({"email": email})

        return {
            "access_token": jwt_token,
            "token_type": "bearer"
        }

    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid Google token")


# =========================
# ✅ FORGOT PASSWORD (OTP + EMAIL)
# =========================
@router.post("/forgot-password")
def forgot_password(email: str, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.email == email).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    otp = str(random.randint(100000, 999999))

    user.otp = otp
    user.otp_expiry = datetime.utcnow() + timedelta(minutes=5)

    db.commit()

    # ✅ EMAIL SEND
    send_otp_email(user.email, otp)

    return {"message": "OTP sent to email"}


# =========================
# ✅ RESET PASSWORD
# =========================
@router.post("/reset-password")
def reset_password(data: ResetPasswordSchema, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.email == data.email).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.otp != data.otp:
        raise HTTPException(status_code=400, detail="Invalid OTP")

    if not user.otp_expiry or datetime.utcnow() > user.otp_expiry:
        raise HTTPException(status_code=400, detail="OTP expired")

    user.password = hash_password(data.new_password)

    # clear OTP
    user.otp = None
    user.otp_expiry = None

    db.commit()

    return {"message": "Password reset successful"}
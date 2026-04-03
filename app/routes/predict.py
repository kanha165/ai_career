from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.user_model import Prediction   # ✅ CORRECT IMPORT
from app.utils.token import verify_token
from app.schemas.skill_schema import SkillInput
from app.services.model_service import predict_top3

router = APIRouter()

# 🔥 DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 🚀 PREDICT API (ML + JWT + DB SAVE)
@router.post("/predict")
def predict(
    data: SkillInput,
    db: Session = Depends(get_db),
    current_user: str = Depends(verify_token)
):
    try:
        # 🔥 ML MODEL (Top 3 prediction)
        results = predict_top3(data.skills)

        # 🔥 SAFE BEST PREDICTION EXTRACTION
        if isinstance(results[0], dict):
            best_prediction = (
                results[0].get("role") or 
                results[0].get("label") or 
                str(results[0])
            )
        else:
            best_prediction = results[0]

        # 🔥 Convert skills list → string
        skills_str = ", ".join(data.skills)

        # 🔥 SAVE TO DATABASE
        new_prediction = Prediction(
            user_email=current_user,
            skills=skills_str,
            prediction=best_prediction
        )

        db.add(new_prediction)
        db.commit()

        return {
            "status": "success",
            "user": current_user,
            "input_skills": data.skills,
            "top_predictions": results,
            "best_match": best_prediction
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/history")
def get_history(
    db: Session = Depends(get_db),
    current_user: str = Depends(verify_token)
):
    data = db.query(Prediction).filter(
        Prediction.user_email == current_user
    ).all()

    return data    
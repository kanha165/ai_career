from fastapi import APIRouter, Depends
from app.utils.token import verify_token

router = APIRouter()

@router.get("/dashboard")
def dashboard(current_user: str = Depends(verify_token)):
    return {
        "message": f"Welcome {current_user}",
        "status": "Authorized"
    }
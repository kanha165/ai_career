from fastapi import APIRouter
from app.services.chatbot_service import get_chatbot_response

router = APIRouter()
router = APIRouter(
    tags=["Chatbot"]   # 🔥 IMPORTANT
)
@router.get("/chat")
def chat(q: str):
    answer = get_chatbot_response(q)
    return {"answer": answer}
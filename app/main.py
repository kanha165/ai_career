from fastapi import FastAPI
from app.database import engine, Base
from app.routes.chatbot import router as chatbot_router
from app.routes.auth import router as auth_router
from app.routes.predict import router as predict_router
from app.routes.protected import router as protected_router
from app.routes.profile import router as profile_router
from app.models import user_model  

app = FastAPI(title="Career Prediction API 🚀")

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "API Running 🚀"}

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(predict_router, prefix="/api", tags=["Prediction"])
app.include_router(protected_router, prefix="/user", tags=["User"])
app.include_router(chatbot_router)



app.include_router(profile_router)
from fastapi.staticfiles import StaticFiles

app.mount("/uploads", StaticFiles(directory="app/uploads"), name="uploads")

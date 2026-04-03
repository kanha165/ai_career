from fastapi import APIRouter, UploadFile, File, Depends
import shutil
import os

router = APIRouter(
    prefix="/profile",
    tags=["Profile"]
)

UPLOAD_DIR = "app/uploads"

# 📤 Upload Profile Pic
@router.post("/upload")
async def upload_profile_pic(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # 👉 yaha DB me save karna hai (user.profile_pic = file_path)

    return {"message": "Profile pic uploaded", "path": file_path}


# ❌ Remove Profile Pic
@router.delete("/remove")
def remove_profile_pic(filename: str):
    file_path = os.path.join(UPLOAD_DIR, filename)

    if os.path.exists(file_path):
        os.remove(file_path)

        # 👉 DB me bhi remove karna hai (user.profile_pic = None)

        return {"message": "Profile pic removed"}
    
    return {"error": "File not found"}
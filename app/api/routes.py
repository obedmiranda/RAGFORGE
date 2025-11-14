from fastapi import APIRouter, UploadFile, File


router = APIRouter(prefix='/api', tags=["PDF"])

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    print(f"📁 Received file: {file.filename}")  # Debug log
    return {"message": f"Hello 👋 {file.filename} uploaded successfully!"}
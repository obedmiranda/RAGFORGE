from fastapi import APIRouter, UploadFile, File
from controllers.pdf_controller import process_pdf_upload

router = APIRouter(prefix='/api', tags=["PDF"])

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
        return await process_pdf_upload(file)
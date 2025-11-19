from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
from controllers.pdf_controller import process_pdf_upload
from controllers.query_controller import query_from_user

router = APIRouter(prefix="/api", tags=["PDF"])

class QueryRequest(BaseModel):
    question: str

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    return await process_pdf_upload(file)

@router.post("/query")
def ask_question(payload: QueryRequest):
    return query_from_user(payload.question)

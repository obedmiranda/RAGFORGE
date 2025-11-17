from fastapi import UploadFile
import uuid
import os
from services.pdf_service import process_document

async def process_pdf_upload(file: UploadFile):
    file_ext = file.filename.split(".")[-1]
    temp_filename = f"/tmp/{uuid.uuid4()}.{file_ext}"
    with open(temp_filename, "wb") as buffer:
        buffer.write(await file.read())

    print("FILE NAME: " + file.filename)
    print("TEMP FILENAME: " + temp_filename)

    # Service Process document (load → split → embed → store)
    result = await process_document(temp_filename, file.filename)

    # print(result)

    if os.path.exists(temp_filename):
        os.remove(temp_filename)

    # Return from the Service PDF
    return result
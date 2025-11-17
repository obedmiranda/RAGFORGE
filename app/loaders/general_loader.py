from loaders.pdf_loader import load_pdf
from loaders.text_loader import load_text
from loaders.docx_loader import load_docx


def load_document(file_path: str):
    ext = file_path.lower().split(".")[-1]

    if ext == "pdf":
        return load_pdf(file_path)
    elif ext == "txt":
        return load_text(file_path)
    elif ext == "docx":
        return load_docx(file_path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")

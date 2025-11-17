import uuid
from loaders.general_loader import load_document
from services.chunks_generator import text_splitter
from services.embedding_service import store_embeddings


async def process_document(path: str, original_name: str):
 
    try:
        docs = load_document(path)
    except Exception as e:
        return {
            "error": f"Loader failed: {str(e)}",
            "status": "failed",
            "filename": original_name
        }

    # No content? Return error.
    if not docs:
        return {
            "error": "No content found. The loader returned 0 documents.",
            "status": "failed",
            "filename": original_name
        }

    print(f"[PDF SERVICE] Loaded {len(docs)} documents.")

    try:
        chunks = text_splitter.split_documents(docs)
    except Exception as e:
        return {
            "error": f"Chunk splitting failed: {str(e)}",
            "status": "failed",
            "filename": original_name
        }

    print(f"[PDF SERVICE] Chunks generated: {len(chunks)}")
    session_id = str(uuid.uuid4())
    document_id = str(uuid.uuid4())
    
    try:
        await store_embeddings(chunks, session_id, document_id)
    except Exception as e:
        return {
            "error": f"Embedding storage failed: {str(e)}",
            "status": "failed",
            "filename": original_name
        }

    print(f"[PDF SERVICE] Stored embeddings into collection: pdf_embeddings_{session_id}")

    return {
        "filename": original_name,
        "pages_detected": len(docs),
        "chunks_generated": len(chunks),
        "collection": session_id,
        "document_id": document_id,
        "status": "indexed"
    }

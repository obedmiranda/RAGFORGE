from dotenv import load_dotenv
import os
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from langchain_postgres.vectorstores import PGVector

load_dotenv()

embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")
CONNECTION_STRING = os.getenv("PGVECTOR_URL")

async def store_embeddings(chunks: list[Document], session_id: str, document_id: str):

    for doc in chunks:
        doc.metadata["session_id"] = session_id
        doc.metadata["document_id"] = document_id
        doc.metadata["source"] = doc.metadata.get("source", "pdf")

    # Guardar en PGVector
    PGVector.from_documents(
        documents=chunks,
        embedding=embedding_model,
        connection_string=CONNECTION_STRING,
        collection_name= "ragforge_embeddings"
          # collection_name=f"pdf_embeddings_{session_id}",
    )

    return {
        "message": "Embeddings stored successfully",
        "chunks_indexed": len(chunks),
        "collection": f"pdf_embeddings_{session_id}"
    }

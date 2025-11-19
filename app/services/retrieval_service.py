from langchain_postgres.vectorstores import PGVector
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

def retrieve_relevant_chunks(query: str, collection_name: str):

    embeddings = OpenAIEmbeddings()

    vectorstore = PGVector(
        connection=os.getenv("PGVECTOR_URL"),
        collection_name=collection_name,
        embeddings=embeddings,
        use_jsonb=os.getenv("PGVECTOR_USE_JSONB", "True").lower() == "true"
    )

    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3}
    )

    relevant_docs = retriever.get_relevant_documents(query)
    print("\n🔍 RETRIEVAL RESULTS")
    print(f"Query: {query}")
    print(f"Collection: {collection_name}")
    print(f"Chunks Retrieved: {len(relevant_docs)}")

    for i, doc in enumerate(relevant_docs, 1):
        print(f"\n--- Chunk {i} ---")
        print(f"Content Preview: {doc.page_content[:200]}...")
        print(f"Metadata: {doc.metadata}")

    return [
        {"content": doc.page_content, "metadata": doc.metadata}
        for doc in relevant_docs
    ]

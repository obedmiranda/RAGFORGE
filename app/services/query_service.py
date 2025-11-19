from services.retrieval_service import retrieve_relevant_chunks

def query_to_ask(query: str):

    print("QUESTION BEING ASKED IN QUERY SERVICE:", query)
    collection_name = "ragforge_embeddings"
    chunks = retrieve_relevant_chunks(query,collection_name)
    dummy_answer = (
        "🔎 This is a mock answer while the LLM chain is not implemented yet.\n\n"
        "Your query was: " + query
    )   

    return {
        "answer": dummy_answer,
        "chunks": chunks
    }

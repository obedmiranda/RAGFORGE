from chains.query_chain import run_qa_chain
from services.rewriter_service import rewrite_query

def query_to_ask(query: str):

    print("QUESTION BEING ASKED IN QUERY SERVICE:", query)

    rewritten = rewrite_query(query)
    print("REWRITTEN QUERY:", rewritten)

    collection_name = "ragforge_embeddings"

    result = run_qa_chain(rewritten, collection_name)

    result["rewritten_query"] = rewritten
    
    return result

from chains.query_chain import run_qa_chain

def query_to_ask(query: str):

    print("QUESTION BEING ASKED IN QUERY SERVICE:", query)
    collection_name = "ragforge_embeddings"

    result = run_qa_chain(query, collection_name)

    return result

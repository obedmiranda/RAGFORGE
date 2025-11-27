from chains.query_chain import (
    retrieve_docs,
    run_qa_with_docs
)

from services.rewriter_service import rewrite_query
from services.multiquery_service import generate_multi_queries
from services.rrf_service import reciprocal_rank_fusion


def query_to_ask(query: str):

    print("ORIGINAL QUERY:", query)

    rewritten = rewrite_query(query)
    print("REWRITTEN QUERY:", rewritten)

    generated_queries = generate_multi_queries(rewritten)
    print("GENERATED MULTI-QUERIES:")
    for q in generated_queries:
        print("   →", q)

    collection_name = "ragforge_embeddings"

    all_results = []
    for q in generated_queries:
        docs = retrieve_docs(q, collection_name)
        all_results.append(docs)

    reranked_docs = reciprocal_rank_fusion(all_results)

    result = run_qa_with_docs(rewritten, reranked_docs)

    result["rewritten_query"] = rewritten
    result["generated_queries"] = generated_queries

    return result

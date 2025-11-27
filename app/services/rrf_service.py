def reciprocal_rank_fusion(results: list[list], k: int = 60):

    # Diccionario para almacenar puntajes acumulados
    fused_scores = {}

    # Diccionario para mapear keys → documento (para evitar colisiones)
    documents = {}

    for docs in results:
        for rank, doc in enumerate(docs):

            # generar una key única por documento
            # (importante para evitar colisiones si el texto es similar)
            key = (doc.page_content[:200] + "_" + str(doc.metadata))

            documents[key] = doc

            # fórmula oficial del paper:
            # score += 1 / (k + rank + 1)
            fused_scores[key] = fused_scores.get(key, 0) + 1 / (k + rank + 1)

    # Ordenar por puntaje RRF descendente
    reranked = sorted(
        fused_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    # Devolver solo los documentos, en orden rerankeado
    return [documents[key] for key, _ in reranked]

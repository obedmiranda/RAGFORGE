Advanced Indexing Optimization Platform for LangChain-based RAG Systems

RAGForge is a modular, extensible framework designed to build enterprise-grade Retrieval-Augmented Generation (RAG) pipelines.
It provides:

⚡ Indexing Optimization Engine
Full vs incremental change detection, selective re-embedding, and chunk-level diffing.

🔍 Retrieval Optimization
Multi-query retrieval, rank fusion, query rewriting, and embedding-based search powered by PGVector.

🧱 Chain Composition Layer
Modular chains for retrieval, generation, ranking, and orchestration.

🖥️ Integrated FastAPI Dashboard
Upload documents, inspect chunks, visualize embeddings, test queries, and monitor RAG performance.

🗄️ PGVector Storage
Efficient vector storage with metadata tracking for document versions and incremental updates.

RAGForge serves as a foundation for building advanced RAG systems, research experiments, or production-ready knowledge assistants.

🚀 Technology Stack

FastAPI for backend + UI

LangChain for retrieval, chains, and orchestration

PGVector for vector storage

OpenAI Embeddings for vector generation

PostgreSQL for metadata + document tracking

Jinja2 Templates for the dashboard

Vanilla JS / HTML / CSS for the frontend

🔧 Current Capabilities

Document upload and chunking

OpenAI embedding generation

Storage in PGVector (persistent)

Retrieval via similarity search

Query endpoint + visual UI

Foundation for chain-based RAG pipelines
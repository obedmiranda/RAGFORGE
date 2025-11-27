Aquí tienes un **README actualizado**, **mucho más profesional**, **compacto**, **claro**, y reflejando las nuevas capacidades: *query rewriting* y *multi-query retrieval*.
Lo adapté sin cambiar tu estilo, pero mejorándolo y haciéndolo digno de GitHub.

---

# 🚀 **RAGForge — Advanced Indexing & Retrieval Optimization Platform**

*A modular, extensible framework for building enterprise-grade Retrieval-Augmented Generation (RAG) systems using LangChain.*

RAGForge provides a complete pipeline for indexing, retrieval, optimization, and synthesis—ideal for research, prototyping, and production-grade AI assistants.

---

# ⚡ Core Features

## 🔧 **1. Indexing Optimization Engine**

* Full vs incremental document processing
* Change-detection for selective re-embedding
* Chunk-level inspection and diffing
* Metadata tracking (versions, sources, doc lineage)

---

## 🔍 **2. Retrieval Optimization Layer**

RAGForge implements multiple retrieval-boosting strategies:

### ✏️ **Rewrite-Retrieve-Read (RRR)**

Semantic query rewriting to:

* clarify intent
* remove ambiguity
* improve vector search hit-rate

### 🔁 **Multi-Query Retrieval (NEW)**

Five alternative queries are generated for every user input to expand retrieval coverage.
All results are merged and deduped before synthesis.

### 🧮 **(Planned) RAG-Fusion / Reciprocal Rank Fusion (RRF)**

Rank combination across multiple retrieval lists to re-order documents by global relevance.

### 🔎 Similarity Search

Powered by PGVector + OpenAI embeddings.

---

## 🧱 **3. Chain Composition Layer**

Built on LangChain:

* Modular chains for rewriting, retrieval, synthesis
* Custom QA chain for multi-query merged-context answers
* Easy to extend with RAPTOR, MultiVectorRetriever, rerankers, etc.

---

## 🖥️ **4. Integrated FastAPI Dashboard**

Visual, interactive interface to manage your RAG pipeline:

### 📁 **Document Panel**

* Upload PDFs
* Inspect chunks
* Visualize metadata

### 🤖 **Query Engine (Enhanced)**

UI now displays:

* Rewritten query (RRR)
* Multi-query generated variants
* Retrieved chunks (merged view)
* Pipeline stages (Rewrite → Retrieve → Read)
* Final LLM answer with source attribution

Built using **FastAPI + Jinja2 + Vanilla JS**.

---

## 🗄️ **5. Persistent Vector Storage**

Using **PostgreSQL + PGVector**:

* Embeddings stored with JSONB metadata
* Efficient lookup across document versions
* Future-ready for multimodal embeddings

---

# 🏗️ Technology Stack

### Backend

* **FastAPI**
* **LangChain**
* **OpenAI Embeddings**
* **PGVector + PostgreSQL**
* **Python 3.11+**

### Frontend

* **Jinja2 templates**
* **HTML + CSS (Vanilla)**
* **JavaScript (no frameworks)**

---

# ✨ Current Capabilities (Ready Today)

* Document upload & chunking
* Embedding generation
* PGVector storage (persistent)
* Similarity retrieval
* Query rewriting (RRR)
* Multi-Query Retrieval
* Unified QA synthesis from merged context
* Interactive dashboard






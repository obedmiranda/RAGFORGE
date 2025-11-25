from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_postgres.vectorstores import PGVector
from langchain.prompts import PromptTemplate
from langchain.schema import Document
from dotenv import load_dotenv
import os

load_dotenv()

def get_vectorstore(collection_name: str):

    embeddings = OpenAIEmbeddings()

    return PGVector(
        connection=os.getenv("PGVECTOR_URL"),
        collection_name=collection_name,
        embeddings=embeddings,
        use_jsonb=os.getenv("PGVECTOR_USE_JSONB", "True").lower() == "true"
    )


def build_qa_chain(collection_name: str):

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    vectorstore = get_vectorstore(collection_name)
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3})

    prompt_template = """
    You are a helpful assistant answering questions about documents.
    Use ONLY the provided context.
    If the answer is not in the context, say you don't have enought context to answer that, ask the user to valid its question, be kind.

    Context:{context}
    Question: {question}
    Answer:
    """

    prompt = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "question"]
    )

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=True
    )

    return chain


def run_qa_chain(query: str, collection_name: str):

    try:
        chain = build_qa_chain(collection_name)
        result = chain.invoke({"query": query})

        answer = result.get("result")
        source_docs = result.get("source_documents", [])

        sources = [
            {
                "content": doc.page_content,
                "metadata": doc.metadata
            }
            for doc in source_docs if isinstance(doc, Document)
        ]

        return {"answer": answer, "sources": sources}

    except Exception as e:
        print("Error running QA chain:", e)
        return {
            "error": str(e),
            "answer": "There was an error running the QA chain.",
            "sources": []
        }

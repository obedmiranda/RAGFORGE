from langchain_openai import ChatOpenAI, OpenAIEmbeddings
# from langchain.chains import RetrievalQA
from langchain_postgres.vectorstores import PGVector
# from langchain.prompts import PromptTemplate
# from langchain.schema import Document

from langchain_classic.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate
from langchain_core.documents import Document

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
    You are an AI assistant that answers questions and generates content using ONLY the information 
    provided in the retrieved document context. 

    You may:
    - Answer factual questions.
    - Synthesize new content (cover letters, summaries, rewrites, paragraphs, drafts).
    - Combine ideas across the context.
    - Rephrase, elaborate, or restructure information.
    - Generate text in any style requested.

    Rules:
    1. You MUST stay grounded in the provided context.
    2. You MUST NOT introduce facts that are not supported by the context.
    3. If the user requests something creative (e.g., a cover letter), generate it using only information found inside the context.
    4. If the context does not contain enough information, politely explain what is missing.
    5. Maintain a helpful, professional tone.

    --------------------
    CONTEXT:
    {context}

    --------------------
    QUESTION:
    {question}

    --------------------
    ANSWER:
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

def retrieve_docs(query: str, collection_name: str, k: int = 3):
     try:
        vectorstore = get_vectorstore(collection_name)
        retriever = vectorstore.as_retriever(
            search_type="similarity",
            search_kwargs={"k": k}
        )
        return retriever.get_relevant_documents(query)
     except Exception as e:
        print("Error in retrieve_docs:", e)
        return []

def run_qa_with_docs(question: str, docs: list[Document]):
    try:
        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

        prompt_template = """
        You are an AI assistant that answers questions and generates content 
        using ONLY the information provided in the retrieved document context.

        --------------------
        CONTEXT:
        {context}

        --------------------
        QUESTION:
        {question}

        --------------------
        ANSWER:
        """

        prompt = PromptTemplate(
            template=prompt_template,
            input_variables=["context", "question"]
        )

        combined_context = "\n\n".join([d.page_content for d in docs])

        formatted = prompt.format(
            context=combined_context,
            question=question
        )

        answer = llm.invoke(formatted)

        return {
            "answer": answer.content,
            "sources": [{"content": d.page_content, "metadata": d.metadata} for d in docs]
        }

    except Exception as e:
        print("Error in run_qa_with_docs:", e)
        return {"answer": "Error.", "sources": []}


     
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

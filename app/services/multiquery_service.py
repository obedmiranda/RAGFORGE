from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.2
)

perspectives_prompt = ChatPromptTemplate.from_template("""
You are an AI assistant. Your task is to generate FIVE different versions of 
the given user question to retrieve relevant documents from a vector database.

Goal:
- Provide multiple perspectives to overcome similarity-search limitations.
- Keep the original intent.
- Do NOT answer the question.
- Just rewrite it 5 times, each one in a separate line.

Original question: {question}
""")

def parse_queries_output(message):
    return message.content.strip().split("\n")

query_gen = perspectives_prompt | llm | parse_queries_output


def generate_multi_queries(question: str) -> list[str]:
   
    try:
        return query_gen.invoke({"question": question})
    except Exception as e:
        print("Multi-query error:", e)
        return [question]

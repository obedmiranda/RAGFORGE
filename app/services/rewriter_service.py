# services/rewriter_service.py

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

rewriter_llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.1
)

rewrite_prompt = ChatPromptTemplate.from_template("""
You rewrite user queries ONLY when beneficial.

RULES:
- If the query is too short, vague, or ambiguous (e.g. “tools?”, “renewable?”, “obed cv”), return it AS-IS.
- If the user does not provide a clear target, return it AS-IS.
- If the query already looks like a valid search question, refine it slightly.
- NEVER insert placeholders like “[something]”.
- NEVER add assumptions.
- NEVER answer the question.
- Your job is ONLY to rewrite for clarity IF POSSIBLE.

Return only the rewritten query (or the original if unclear).

User query:
{query}
""")

def rewrite_query(query: str) -> str:
    try:
        # Very short queries? → Skip rewrite
        if len(query.split()) < 3:
            return query

        prompt = rewrite_prompt.format_messages(query=query)
        response = rewriter_llm.invoke(prompt)
        rewritten = response.content.strip()

        if not rewritten:
            return query

        return rewritten
    except Exception as e:
        print("Rewrite Error:", e)
        return query

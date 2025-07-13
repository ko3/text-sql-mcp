# app/core/llm.py

from openai import OpenAI
from app.core.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def generate_sql_prompt(question: str, table_contexts: list) -> str:
    context = "\n".join(table_contexts)
    return f"""You are a helpful assistant. Convert the user's question to a SQL query.

Available tables:
{context}

User question:
{question}

SQL query:
"""

def call_llm(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You generate SQL from text given table schemas."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )
    return response.choices[0].message.content.strip()

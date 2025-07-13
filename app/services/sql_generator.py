from app.core.vector_store import qdrant
from app.core.embeddings import get_embedding
from app.core.llm import generate_sql_prompt, call_llm
from app.core.config import settings

def handle_text_to_sql(query):
    query_vector = get_embedding(query.question)
    hits = qdrant.search(
        collection_name=settings.COLLECTION_NAME,
        query_vector=query_vector,
        limit=3
    )
    table_contexts = [hit.payload['text'] for hit in hits]
    prompt = generate_sql_prompt(query.question, table_contexts)
    sql = call_llm(prompt)
    return {"sql": sql.strip(), "tables_used": table_contexts}
from app.core.vector_store import qdrant
from app.core.embeddings import get_embedding
from qdrant_client.models import PointStruct
import uuid

def embed_and_store_schema(schema):
    table_text = f"Table: {schema.table_name}, Columns: {', '.join(schema.columns)}"
    vector = get_embedding(table_text)
    point = PointStruct(
        id=str(uuid.uuid4()),
        vector=vector,
        payload={"table": schema.table_name, "text": table_text}
    )
    qdrant.upsert(
        collection_name="table_schemas",
        points=[point]
    )
    return {"status": "ok", "table": schema.table_name}
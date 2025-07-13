from fastapi import APIRouter
from app.models.schema import SchemaInput, QueryInput
from app.services.schema_embedder import embed_and_store_schema
from app.services.sql_generator import handle_text_to_sql

router = APIRouter()

@router.post("/ingest_schema")
def ingest(schema: SchemaInput):
    return embed_and_store_schema(schema)

@router.post("/text_to_sql")
def text_to_sql(query: QueryInput):
    print("inside text_to_sql")
    return handle_text_to_sql(query)

from pydantic import BaseModel
from typing import List

class SchemaInput(BaseModel):
    table_name: str
    columns: List[str]

class QueryInput(BaseModel):
    question: str
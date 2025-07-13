from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="MCP Text-to-SQL Server")
app.include_router(router)

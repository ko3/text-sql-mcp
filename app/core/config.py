from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    OPENAI_API_KEY: str
    QDRANT_URL: str
    QDRANT_API_KEY: str
    COLLECTION_NAME: str = "table_schemas"

    class Config:
        env_file = ".env"

settings = Settings()

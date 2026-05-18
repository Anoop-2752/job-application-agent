from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # LLM
    groq_api_key: str
    groq_model: str = "llama-3.3-70b-versatile"

    # Search
    serpapi_key: str = ""

    # Email
    gmail_user: str = ""
    gmail_app_password: str = ""

    # LangSmith
    langchain_api_key: str = ""
    langchain_tracing_v2: str = "true"
    langchain_project: str = "job-application-agent"


@lru_cache()
def get_settings() -> Settings:
    return Settings()
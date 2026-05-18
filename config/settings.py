from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    # LLM
    groq_api_key: str
    groq_model: str = "llama-3.3-70b-versatile"

    # Search
    serpapi_key: str = ""          # optional — we'll add DuckDuckGo fallback

    # Email (Gmail SMTP)
    gmail_user: str = ""
    gmail_app_password: str = ""   # not your real password — Gmail App Password

    # LangSmith tracing (free tier)
    langchain_api_key: str = ""
    langchain_tracing_v2: str = "true"
    langchain_project: str = "job-application-agent"

    class Config:
        env_file = ".env"
        extra = "ignore"            # don't crash on unknown env vars


@lru_cache()
def get_settings() -> Settings:
    return Settings()
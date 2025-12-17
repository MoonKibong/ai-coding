"""Application configuration."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""
    app_name: str = "MediPredict Lite API"
    app_version: str = "0.1.0"
    debug: bool = False
    
    # API settings
    api_v1_prefix: str = "/api/v1"
    
    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()


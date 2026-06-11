import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Ronex AI Backend"
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))
    ALLOWED_ORIGINS: str = os.getenv("ALLOWED_ORIGINS", "*")
    
    # Internal credentials masked away from web and mobile clients
    UPSTREAM_PROVIDER_API_KEY: str = os.getenv("UPSTREAM_PROVIDER_API_KEY", "ronex_default_production_secure_token")

settings = Settings()

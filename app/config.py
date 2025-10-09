from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    """Application settings"""
    
    # Supabase Configuration
    supabase_url: str = ""
    supabase_key: str = ""
    supabase_service_key: str = ""
    
    # Database Configuration
    database_url: str = ""
    
    # Application Configuration
    app_name: str = "VitalApp Backend"
    app_version: str = "1.0.0"
    debug: bool = True
    
    # API Configuration
    api_prefix: str = "/api/v1"
    
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False
    )


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance"""
    return Settings()

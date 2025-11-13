from pydantic_settings import BaseSettings
from typing import List, Optional
import os


class Settings(BaseSettings):
    """Application settings"""
    
    # Project
    PROJECT_NAME: str = "Commons Ledger"
    API_V1_PREFIX: str = "/api/v1"
    DEBUG: bool = False
    RELOAD: bool = False
    LOG_LEVEL: str = "INFO"
    
    # Database
    DATABASE_URL: str
    DATABASE_HOST: str = "localhost"
    DATABASE_PORT: int = 5432
    DATABASE_NAME: str = "commons_ledger"
    DATABASE_USER: str = "commons"
    DATABASE_PASSWORD: str
    
    # Redis
    REDIS_URL: str
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    
    # MinIO
    MINIO_ENDPOINT: str
    MINIO_ACCESS_KEY: str
    MINIO_SECRET_KEY: str
    MINIO_BUCKET: str = "commons-ledger"
    MINIO_USE_SSL: bool = False
    
    # JWT Authentication
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS
    CORS_ORIGINS: List[str] = ["http://localhost:3000"]
    
    # ML Models
    MODEL_PATH: str = "/app/models"
    ENABLE_ML_FEATURES: bool = True
    
    # OCR
    TESSERACT_PATH: str = "/usr/bin/tesseract"
    OCR_LANGUAGE: str = "eng"
    OCR_TIMEOUT: int = 30
    
    # Celery
    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str
    
    # File Upload
    MAX_UPLOAD_SIZE_MB: int = 10
    ALLOWED_FILE_TYPES: List[str] = ["pdf", "jpg", "jpeg", "png"]
    
    # Feature Flags
    ENABLE_INVOICE_FINANCING: bool = True
    ENABLE_CREDIT_SCORING: bool = True
    ENABLE_CASHFLOW_FORECASTING: bool = True
    ENABLE_ATTESTATIONS: bool = True
    ENABLE_KYC_LITE: bool = True
    
    # IPFS (Optional)
    ENABLE_IPFS: bool = False
    IPFS_HOST: str = "localhost"
    IPFS_PORT: int = 5001
    
    # Email (Optional)
    SMTP_HOST: Optional[str] = None
    SMTP_PORT: int = 587
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    SMTP_FROM_EMAIL: str = "noreply@commonsledger.local"
    
    # Security
    ENABLE_ENCRYPTION: bool = True
    ENCRYPTION_KEY: Optional[str] = None
    
    # Audit
    ENABLE_AUDIT_LOGGING: bool = True
    AUDIT_LOG_RETENTION_DAYS: int = 365
    
    # Rate Limiting
    RATE_LIMIT_PER_MINUTE: int = 60
    RATE_LIMIT_BURST: int = 10
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()

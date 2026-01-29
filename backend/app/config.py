from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "mysql+pymysql://root:root@localhost/job_scam_detection"  # Update with your MySQL credentials

    class Config:
        env_file = ".env"

settings = Settings()
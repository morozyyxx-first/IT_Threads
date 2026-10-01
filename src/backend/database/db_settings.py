import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
load_dotenv()

class DBSettings(BaseSettings):
    DB_URL: str = os.getenv("DB_URL")

db_settings = DBSettings()
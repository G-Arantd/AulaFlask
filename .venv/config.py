import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY: str = os.getenv("SECRET_KEY")
DATABASE_URL: str = os.getenv("DATABASE_URL")
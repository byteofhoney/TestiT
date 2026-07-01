import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")

if not MONGO_URI:
    raise ValueError("MONGO_URI not found. Check your .env file.")
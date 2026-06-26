import os

db_password = os.getenv("DB_PASSWORD")

print("Password Database:", db_password)

from dotenv import load_dotenv
import os

load_dotenv()

db_password = os.getenv("DB_PASSWORD")

print("Password Database:", db_password)
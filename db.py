import os
import psycopg

DATABASE_URL = os.environ.get("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL not set")

def get_connection():
    return psycopg.connect(DATABASE_URL)
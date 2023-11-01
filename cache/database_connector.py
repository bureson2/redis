import psycopg2
import redis
import os
from dotenv import load_dotenv

load_dotenv()

def get_pg_connection():
    POSTGRES_NAME = os.getenv("POSTGRES_NAME")
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT")

    return psycopg2.connect(
        dbname=POSTGRES_NAME,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        host=POSTGRES_HOST,
        port=POSTGRES_PORT
    )

def get_redis_connection():
    REDIS_NAME = os.getenv("REDIS_NAME")
    REDIS_USER = os.getenv("REDIS_USER")
    REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")
    REDIS_HOST = os.getenv("REDIS_HOST")
    REDIS_PORT = os.getenv("REDIS_PORT")

    return redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_NAME, password=REDIS_PASSWORD)

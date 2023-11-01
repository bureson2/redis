import psycopg2
from database_connector import get_pg_connection

conn = get_pg_connection()
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT
);
""")

cursor.execute("""
CREATE TABLE ingredients (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    quantity VARCHAR(255),
    recipe_id INTEGER REFERENCES recipes(id)
);
""")

conn.commit()
cursor.close()
conn.close()

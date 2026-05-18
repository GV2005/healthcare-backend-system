import os
import psycopg2

database_url = os.getenv("DATABASE_URL")

print(database_url)

conn = psycopg2.connect(database_url)

print("DATABASE CONNECTED")

cursor = conn.cursor()
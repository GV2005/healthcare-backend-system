import psycopg2
import os

database_url = os.getenv("DATABASE_URL")
conn=psycopg2.connect(database_url)
cursor=conn.cursor()

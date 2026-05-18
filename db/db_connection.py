import psycopg2
import os

database_url = os.getenv("postgresql://gv2005:sFOQlKIOKINUU5n4g6gQEH7aqTxo2a3C@dpg-d85ho4j7uimc739hkgq0-a/healthcare_db_v0no")
conn=psycopg2.connect(database_url)
cursor=conn.cursor()

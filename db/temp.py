import psycopg2

database_url = "postgresql://gv2005:sFOQlKIOKINUU5n4g6gQEH7aqTxo2a3C@dpg-d85ho4j7uimc739hkgq0-a.oregon-postgres.render.com/healthcare_db_v0no"

conn = psycopg2.connect(database_url)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS illnesses(
    id SERIAL PRIMARY KEY,
    illness VARCHAR(100) NOT NULL
)
""")

conn.commit()

print("tables created")
import psycopg2

database_url = "postgresql://gv2005:sFOQlKIOKINUU5n4g6gQEH7aqTxo2a3C@dpg-d85ho4j7uimc739hkgq0-a.oregon-postgres.render.com/healthcare_db_v0no"

conn = psycopg2.connect(database_url)

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS illnesses(
        id SERIAL PRIMARY KEY,
        illness VARCHAR(100) NOT NULL
    )
''')
conn.commit()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS patients(
        id SERIAL PRIMARY KEY,
        patient_name VARCHAR(100) NOT NULL,
        illness_id INT,

        FOREIGN KEY (illness_id)
        REFERENCES illnesses(id)
    )
''')
conn.commit()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS doctors(
        id SERIAL PRIMARY KEY,
        doctor_name VARCHAR(100) NOT NULL,
        specialization VARCHAR(100)
    )
''')
conn.commit()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS appointments(
        id SERIAL PRIMARY KEY,
        patient_id INT,
        doctor_id INT,
        date DATE,
        time TIME,
        status VARCHAR(50),

        FOREIGN KEY (patient_id)
        REFERENCES patients(id),

        FOREIGN KEY (doctor_id)
        REFERENCES doctors(id)
    )
''')
conn.commit()

print("tables created")
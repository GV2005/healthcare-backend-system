from db_connection import cursor, conn


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
from fastapi import APIRouter
from schemas.patient_schema import PatientResponse,PatientRequest
from db.db_connection import conn,cursor

router=APIRouter()

@router.post("/patients")

def add_patients(patient:PatientRequest):
    cursor.execute('''INSERT INTO patients(patient_name,illness_id)
                   VALUES (%s,%s)''',(patient.patient_name,patient.illness_id))
    conn.commit()
    return {"message":"patient added successfully"}

@router.get("/patients",response_model=list[PatientResponse])

def get_patients():
    cursor.execute('''SELECT * FROM patients''')
    rows=cursor.fetchall()
    return [{"id":row[0],"patient_name":row[1],"illness_id":row[2]} for row in rows]


from fastapi import APIRouter
from schemas.doctor_schema import DoctorRequest,DoctorResponse
from db.db_connection import conn,cursor

router=APIRouter()

@router.post("/doctors")

def add_doctor(doctor:DoctorRequest):
    cursor.execute('''INSERT INTO doctors(doctor_name,specialization)
                   VALUES (%s,%s)''',(doctor.doctor_name,doctor.specialization))
    conn.commit()
    return {"message":"doctor added successfully"}

@router.get("/doctors",response_model=list[DoctorResponse])

def get_doctors():
    cursor.execute('''SELECT * FROM doctors''')
    rows=cursor.fetchall()
    return [{"id":row[0],"doctor_name":row[1],"specialization":row[2]} for row in rows]


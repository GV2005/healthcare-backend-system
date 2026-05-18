from fastapi import APIRouter
from schemas.appointment_schema import AppointmentRequest,AppointmentResponse
from db.db_connection import conn,cursor

router=APIRouter()

@router.post("/appointments")

def add_appointment(appointment:AppointmentRequest):
    cursor.execute('''INSERT INTO appointments(patient_id,doctor_id,date,time,status)
                   VALUES (%s,%s,%s,%s,%s)''',(appointment.patient_id,appointment.doctor_id,appointment.date,appointment.time,appointment.status))
    conn.commit()
    return {"message":"Appointment booked successfully"}

@router.get("/appointments",response_model=list[AppointmentResponse])

def get_patients():
    cursor.execute('''SELECT * FROM appointments''')
    rows=cursor.fetchall()
    return [{"id":row[0],"patient_id":row[1],"doctor_id":row[2],"date":row[3],"time":row[4],"status":row[5]} for row in rows]


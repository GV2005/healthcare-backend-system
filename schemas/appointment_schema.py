from pydantic import BaseModel
from datetime import date,time

class AppointmentRequest(BaseModel):
    patient_id:int
    doctor_id:int
    date:date
    time:time
    status:str

class AppointmentResponse(BaseModel):
    id:int
    patient_id:int
    doctor_id:int
    date:date
    time:time
    status:str

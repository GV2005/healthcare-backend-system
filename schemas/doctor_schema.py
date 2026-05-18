from pydantic import BaseModel

class DoctorRequest(BaseModel):
    doctor_name:str
    specialization:str

class DoctorResponse(BaseModel):
    id:int
    doctor_name:str
    specialization:str

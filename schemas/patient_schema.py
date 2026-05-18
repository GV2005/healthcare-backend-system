from pydantic import BaseModel

class PatientRequest(BaseModel):
    patient_name:str
    illness_id:int

class PatientResponse(BaseModel):
    id:int
    patient_name:str
    illness_id:int

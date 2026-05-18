from pydantic import BaseModel

class IllnessesRequest(BaseModel):
    illness_name:str

class IllnessesResponse(BaseModel):
    id:int
    illness_name:str

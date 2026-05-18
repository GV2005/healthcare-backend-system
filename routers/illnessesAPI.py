from fastapi import APIRouter
from schemas.illness_schema import IllnessesRequest,IllnessesResponse
from db.db_connection import conn,cursor

router=APIRouter()

@router.post("/illnesses")

def add_illness(illness:IllnessesRequest):
    cursor.execute('''INSERT INTO illnesses(illness)
                   VALUES (%s)''',(illness.illness_name,))
    conn.commit()
    return {"message":"illness added successfully"}

@router.get("/illnesses",response_model=list[IllnessesResponse])

def get_illnesses():
    cursor.execute('''SELECT * FROM illnesses''')
    rows=cursor.fetchall()
    return [{"id":row[0],"illness_name":row[1]} for row in rows]


from fastapi import FastAPI,HTTPException
from db.create_tables import *
from middleware.logging_middleware import log_requests
from exceptionHandlers.exphandler import http_exception_handler
from routers.patientAPI import router as router1
from routers.doctorAPI import router as router2
from routers.illnessesAPI import router as router3
from routers.appointmentAPI import router as router4

app=FastAPI()

app.include_router(router1)
app.include_router(router2)
app.include_router(router3)
app.include_router(router4)
app.middleware("http")(log_requests)
app.exception_handler(HTTPException)(http_exception_handler)
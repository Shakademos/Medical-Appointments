from fastapi import  FastAPI
from Router.patients import patient_router
from Router.doctor import Doctor_router
from Router.appointment import appointment_router


app = FastAPI()

app.include_router(patient_router)
app.include_router(Doctor_router)
app.include_router(appointment_router)

@app.get('/')
def home():
    return 'Welcome'
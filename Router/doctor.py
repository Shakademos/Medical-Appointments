from fastapi import APIRouter, HTTPException
from typing import Dict
from schemas.doctors import Docs

doctor_db: Dict[int, Docs] = {}

Doctor_router = APIRouter()




#create
@Doctor_router.post("/doctor/")
def create_doctor(doctor: Docs):
    if doctor.id in doctor_db:
        raise HTTPException(status_code=404, detail="Doctor already exists")
    doctor_db[doctor.id] = doctor
    return doctor

#Read
@Doctor_router.get("/doctor/{doctor_id}")
def Read_doctor(doctor_id:int):
    if doctor_id not in doctor_db:
        raise HTTPException(status_code=404, detail= "Doctor not found")
    return doctor_db[doctor_id]

#Update
@Doctor_router.put("/doctor/{doctor_id}")
def update_doctor(doctor_id: int, doctor:Docs):
    if doctor_id not in doctor_db:
        raise HTTPException(status_code=404, detail= 'Doctor not found')
    doctor_db[doctor_id] = doctor
    return doctor

#Delet
@Doctor_router.delete("/doctor/{doctor_id}")
def Delet_doctor(doctor_id:int):
    if doctor_id not in doctor_db:
        raise HTTPException(status_code=404, detail=' Doctor not found')
    del doctor_db[doctor_id]
    return {"message": "Doctor deleted"}
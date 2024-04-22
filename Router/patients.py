from fastapi import APIRouter, HTTPException
from typing import Dict
from schemas.patient import Patients

patients_db: Dict[int, Patients] = {}



patient_router = APIRouter()




#create
@patient_router.post("/patients/")
def create_patint(patient: Patients):
    patients_db[patient.id] = patient
    return patient

#Read
@patient_router.get("/patients/{patient_id}")
def Read_patient(patient_id:int):
    if patient_id not in patients_db:
        raise HTTPException(status_code=404, detail= "Patient not found")
    return patients_db[patient_id]

#Update
@patient_router.put("/patients/{patient_id}")
def update_patient(patient_id: int, patient:Patients):
    if patient_id not in patients_db:
        raise HTTPException(status_code=404, detail= 'patient not found')
    patients_db[patient_id] = patient
    return patient

#Delet
@patient_router.delete("/patients/{patient_id}")
def Delet_patient(patient_id:int):
    if patient_id not in patients_db:
        raise HTTPException(status_code=404, detail=' patient not found')
    del patients_db[patient_id]
    return {"message": "Patient deleted"}
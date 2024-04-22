from fastapi import APIRouter, HTTPException
from schemas.appointment import Appointments
from schemas.patient import Patients
from schemas.doctors import Docs
from typing import Dict


appointment_db: dict[int, Appointments] = {}
doctor_db: Dict[int, Docs] = {}
patients_db: Dict[int, Patients] = {}
appointment_db_counter = 1


appointment_router = APIRouter()
#create an appointment
@appointment_router.post('/apointment/')
def Create_appointment(patient_id: int):
    global appointment_db_counter
    if patient_id not in patients_db:
         raise HTTPException(status_code=404, detail='Patient not found')
    available_doctor = [doctor for doctor in doctor_db.values () if doctor['is_available']]
    if not available_doctor:
        raise HTTPException (status_code=400, detail= 'No available Doctor')
    first_available_doctor = available_doctor[0]
    new_appointment = Appointments(id= appointment_db_counter, patient= patients_db [patient_id], doctor=doctor_db, date= '2024-04-21')
    appointment_db[appointment_db_counter] = new_appointment
    appointment_db_counter = +1
    first_available_doctor.is_available
    return new_appointment

#complete an appintment
@appointment_router.put('/appointment/{appointment_id}')
def complet_appointment(appointment_id:int):
    if appointment_id not in appointment_db:
        raise HTTPException(status_code=404, detail=' Appointmine not found')
    completed_appointment = appointment_db[appointment_id]
    completed_appointment.doctor.is_available = True
    return completed_appointment

#cancel an appointment 
@appointment_router.delete('/appointment/{appointment_id}')
def cancel_appointment(appointment_id:int):
    if appointment_id not in appointment_db:
        raise HTTPException(status_code=404, detail=' Appointmine not found')
    cancel_appointment = appointment_db[appointment_id]
    cancel_appointment.doctor.is_available = True
    del appointment_db[appointment_id]
    return {'Message': 'Apointment Canceled'}

#Availability statuse for Doctor
@appointment_router.put('/doctor/{doctor_id},/ availability_id/{is_available}')
def availability_of_doctor(doctor_id:int, is_available:bool ):
     if doctor_id not in doctor_db:
        raise HTTPException(status_code=404, detail='Doctor not Available')
     doctor_db[doctor_id].is_available = is_available
     return doctor_db[doctor_id]

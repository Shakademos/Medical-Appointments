from pydantic import BaseModel
from typing import Dict

class Patients(BaseModel):
    id: int
    name: str
    age: int
    sex: str
    weight: float
    height: float
    phone: int

class PatientsCreate(BaseModel):
    name: str
    age: int
    sex: str
    weight: float
    height: float
    phone: int

new_patient = Patients(
    id=456, 
    name='Oluwasheun', 
    age=34, 
    sex='Male', 
    weight=85.8, 
    height=5.5, 
    phone= 81689647
)

   
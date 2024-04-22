from pydantic import  BaseModel
from datetime import datetime


class Appointments(BaseModel):
    id: int
    patient: str
    doctor: str
    date: str


new_appointment = Appointments(
    id = 23,
    patient= 'Bola', 
    doctor= 'Dr Aladed', 
    date= '2024/04/22'
)
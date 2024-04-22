from pydantic import BaseModel

class Docs(BaseModel):
    id: int
    name: str 
    specialization: str 
    phone: int
    is_available:bool = True


new_doctor = Docs(
    id= 45278, 
    name='Dr James', 
    specialization='Dentist', 
    phone= 2348956486
)
from pydantic import BaseModel
from datetime import date

class register(BaseModel):
    name : str
    email : str
    password : str
    role : str

class login(BaseModel):
    email : str
    password : str

class add(BaseModel):
    name : str
    specialization : str
    experience_years : int

class appointment(BaseModel):
    doctor_id : int
    patient_id : int
    date : date
    time_slot : str

class update(BaseModel):
    status : str
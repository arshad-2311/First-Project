from fastapi import FastAPI, Depends
from typing import Annotated
import models
from database import engine, Sessionlocal
from sqlalchemy.orm import Session
import schema

app = FastAPI()

models.Base.metadata.create_all(bind = engine)

def get_db():
    db = Sessionlocal()
    try:
        yield db
    
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/register")
async def create_user(register: schema.register, db: db_dependency):
    existing_user = db.query(models.users).filter(models.users.email == register.email).first()
    
    if existing_user:
        return {
            "success": False,
            "message": "Email already exists"
        }
    
    db_post = models.users(**register.dict())
    db.add(db_post)
    db.commit()
    print("inserted user", db_post.__dict__)
    return {
        'message' : 'User registered successfully',
        "user-id" : db_post.id
    }

@app.post("/login")
async def login_user(login: schema.login, db: db_dependency):
    existing_user = db.query(models.users).filter(models.users.email == login.email).first()
    passowrd = db.query(models.users).filter(models.users.password == login.password).first()

    if existing_user:
        if passowrd:
            return{
                'message': 'Login successful', 
                'token': '<jwt_token>'
            }
        
    return {'email or password wrong or maybe you did not registered'}

@app.post("/doctor/profile")
async def add_doctor(add: schema.add, db: db_dependency):
    db_add = models.doctors(**add.dict())
    db.add(db_add)
    db.commit()
    return{
        'message' : 'doctor profile created',
        'doctor_id' : db_add.id
    }

@app.get("/doctors")
async def get_doctors(db: db_dependency):
    display = db.query(models.doctors).all()
    result = []

    for i in display:
        result.append({
            'Id': i.id,
            'Name': i.name,
            'Specialization': i.specialization,
            'Experience': i.experience_years
        })

    return result

@app.post("/appointments/book")
async def book_appointment(appointment: schema.appointment, db: db_dependency):
    prev_appointment = db.query(models.appointments).filter(models.appointments.time_slot == appointment.time_slot).first()
    
    if prev_appointment:
        return{'given time already booked by another'}
    
    
    db_app = models.appointments(**appointment.dict())
    db.add(db_app)
    db.commit()
    return{'message': 'Appointment booked', 'appointment_id': 100 + db_app.id}

@app.get("/appointments/patient/{patient_id}")
async def view_patient_appointment(patient_id : int, db: db_dependency):
    appointments = db.query(models.appointments).all()
    doctors = db.query(models.doctors).all()
    result = []

    for appointment in appointments:
        if appointment.patient_id == patient_id:
            for doctor in doctors:
                if doctor.id == appointment.doctor_id:
                    result.append({
                        'appointment_id': 100 + appointment.id,
                        'doctor name': doctor.name,
                        'date': appointment.date,
                        'time slot': appointment.time_slot,
                        'status': appointment.status
                    })

    return result

    
@app.get("/appointments/doctor/{doctor_id}")
async def view_doctor_appointments(doctor_id: int,db: db_dependency):
    patients = db.query(models.users).all()
    appointments = db.query(models.appointments).all()
    result = []

    for appointment in appointments:
        if appointment.doctor_id == doctor_id:
            for patient in patients:
                if patient.id == appointment.patient_id:
                    result.append({
                        'appointment_id': 100 + appointment.id,
                        'patient name': patient.name,
                        'date':appointment.date,
                        'time slot': appointment.time_slot,
                        'status':appointment.status
                    })
    
    return result

@app.put("/appointments/{appointment_id}")
async def update_status(appointment_id : int, update : schema.update, db : db_dependency):
    appointment = db.query(models.appointments).filter(models.appointments.id == appointment_id).first()

    if appointment is None:
        return{'cannot update it'}
    
    appointment.status = update.status
    db.commit()
    db.refresh(appointment)
    return {'message': 'Appointment updated'}

@app.delete("/appointments/{appointment_id}")
async def delete_appointment(appointment_id: int, db: db_dependency):
    delete_app =db.query(models.appointments).filter(models.appointments.id == appointment_id).first()

    if delete_app is None:
        return{'message' : 'no data is there given appointment id'}
    
    db.delete(delete_app)
    db.commit()
    return {'message': 'appointment deleted successfully'}

@app.get("/doctors/search")
async def list_doc(db : db_dependency, specialization : str):
    view_doc = db.query(models.doctors).all()
    result = []

    for doctor in view_doc:
        if doctor.specialization == specialization:
            result.append({
                'id': doctor.id,
                'name' : doctor.name,
                'specialization' : doctor.specialization,
                'experience_years' : doctor.experience_years
            })

    return result

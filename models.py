from sqlalchemy import Boolean, Column, String, Integer, ForeignKey
from database import Base

class users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100), unique=True)
    password = Column(String(255))
    role = Column(String(20))

class doctors(Base):
    __tablename__ = 'doctors'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    specialization = Column(String(100))
    experience_years = Column(Integer)

class appointments(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True, index=True)
    doctor_id = Column(Integer, ForeignKey('doctors.id'))
    patient_id = Column(Integer, ForeignKey('users.id'))
    date = Column(String(10))
    time_slot = Column(String(11))
    status = Column(String(15), default='Confirmed')
program files are inside env firectory
the files are
- main.py
- models.py
- database.py
- schema.py

database files are:
- data.sql

# Doctor Appointment System (FastAPI)

A RESTful API for managing doctor appointments, built with FastAPI and MySQL.

## Features

- User registration and login
- Doctor profile management
- Appointment booking and management
- View appointments (for both patients and doctors)
- Search doctors by specialization
- Appointment status updates

## Technologies Used

- Python 3.x
- FastAPI
- SQLAlchemy (ORM)
- MySQL
- Pydantic (Data validation)
- Uvicorn (ASGI server)

## Prerequisites

- Python 3.7+
- MySQL Server
- pip (Python package manager)

## installations
    [In Terminal]
 -pip install -r requirements.txt

    (or)

pip install fastapi uvicorn sqlalchemy pymysql pydantic

## environment

create:

 python  -m venv env  

activate :

  .\venv\Scripts\activate 

## Set up MySQL database:

Create a database named sqldb

Update the connection URL in database.py with your credentials:

-URL_DATABASE = "mysql+mysqlconnector://root:yourpassword@localhost/sqldb"

## Running the Application
Start the development server:

uvicorn main:app --reload
The API will be available at:

http://127.0.0.1:8000

Interactive API docs: http://127.0.0.1:8000/docs



*****  check well that you are currently correct directory *****

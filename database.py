from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#mysql+mysqlconnector://<username>:<password>@<host>/<database>
URL_DATABASE = "mysql+mysqlconnector://root:intern@Arshad/sqldb"

engine = create_engine(URL_DATABASE, pool_size= 20, max_overflow= 30)

Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind= engine)

Base = declarative_base()
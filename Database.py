import json 
import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Leer config desde el JSON
with open('db_config.json', 'r') as json_file:
    data = json.load(json_file)
    usuario = data["user"]
    password = data["passwd"]
    server = data["server"]
    database = data["database"]

db_url = f"mysql+pymysql://{usuario}:{password}@{server}/{database}"
Base = declarative_base()


class Airbnb(Base):

    __tablename__ = "Airbnb_Data"
    airbnb_id = Column("airbnb_id", Integer, primary_key=True)
    name = Column("name", String(150))
    host_id = Column("host_id", Integer)
    host_identity_verified = Column("host_identity_verified", Boolean)
    host_name = Column("host_name", String(50))
    neighbourhood_group = Column("neighbourhood_group", String(50))
    neighbourhood = Column("neighbourhood", String(50))
    latitude = Column("latitude", Integer)
    longitude = Column("longitude", Integer)
    country = Column("country", String(20))
    country_code = Column("country_code", String(3))
    instant_bookable  = Column("instant_bookable ", Boolean)
    cancellation_policy = Column("cancellation_policy", String(10))
    room_type  = Column("room_type ", String(20))
    construction_year = Column("construction_year ", Date)
    price = Column("price", Integer)
    service_fee = Column("service_fee", Integer)
    minimum_night = Column("minimum_night", Integer)
    number_of_reviews = Column("number_of_reviews", Integer)
    last_review = Column("last_review", Date)
    reviews_per_month = Column("reviews_per_month ", Integer)
    reviews_rate_number = Column("reviews_rate_number", Integer)
    availability_365 = Column("availability_365", Integer)
    house_rules = Column("house_rules", Text) 

    def __init__ (self, session):
        self.session = session

    #Create a new Airbnb, new_airbnb should bring all the information preferably in a dictionary.
    def create(self, new_airbnb):
        self.session.add(new_airbnb)
        self.session.commit()
    
    #Update an Airbnb, update_data must bring all the information to update
    def update(self, update_data):
        for key, value in update_data.items():
            setattr(self, key, value)
        self.session.commit()

    #Delete rows, requires Airbnb ID
    def delete(self, airbnb_id):
        self.session.delete(airbnb_id)
        self.session.commit()

#Function to Create Engine
def creating_engine():
    engine = create_engine(db_url)
    return engine

#Function to create the sessions
def creating_session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

#Function to close the session
def closing_session(session):
    session.close()





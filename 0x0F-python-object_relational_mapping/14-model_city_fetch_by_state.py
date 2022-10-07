#!/usr/bin/python3
""" Lists all State objects from the database hbtn_0e_6_usa
"""


import sys
from model_state import Base, State
from model_city import Base, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    city_state = session.query(City, State).\
            filter(City.state_id==State.id).all()

    for city, state in city_state:
        print(f'{state.name}: ({city.id}) {city.name}')

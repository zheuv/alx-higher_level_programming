#!/usr/bin/python3
""" this script lists the cities in the cities table """

from model_city import City
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    instances = session.query(City, State).\
        join(State, State.id == City.state_id).all()
    if instances:
        for city, state in instances:
            print(f"{state.name}: ({city.id}) {city.name}")
    engine.dispose()
    session.close()

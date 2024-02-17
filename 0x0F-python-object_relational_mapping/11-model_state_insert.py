#!/usr/bin/python3
""" this script adds a state to the states table """

from model_state import Base, State
from sqlalchemy.orm import (create_engine)
from sqlalchemy import sessionmaker
import sys
if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    new_state = State(name="Louisiana")
    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(new_state)
    new_state_id = session.query(State).filter_by(State.name="Louisiana").first()
    print(new_state_id)
    engine.dispose()

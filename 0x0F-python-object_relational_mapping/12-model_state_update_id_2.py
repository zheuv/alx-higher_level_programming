#!/usr/bin/python3
""" this scripts updats the state with the id 2 """

from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlachemy.orm import sessionmaker
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
    instance = session.query(State).filter(State.id == 2).first()
    instance.name = "New Mexico"
    session.commit()
    engine.dispose()

#!/usr/bin/python3

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
import sys

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Session = sessionmaker(engine)
    session = Session()
    first = session.query(State).first()
    if first:
        print ("{}: {}".format(first.id, first.name))

    else: 
        pass
    engine.dispose()


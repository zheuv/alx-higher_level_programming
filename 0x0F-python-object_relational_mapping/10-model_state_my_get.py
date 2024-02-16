#!/usr/bin/python3
""" this script prints the id of the name the user gave """
from sqlalchemy import func
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
    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.query(State).filter(func.binary(State.name).like('%{}%'.format(sys.argv[4]))).first()
    if instance:
        print(instance.id)
    else:
        print("Not found")
    engine.dispose()


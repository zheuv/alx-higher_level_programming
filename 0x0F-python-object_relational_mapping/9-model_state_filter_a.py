#!/usr/bin/python3
""" this script prints the states with the letter a using ORM """
from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the states with names containing the letter 'a' and order by id
    for state in session.query(State).filter(State.name.like('%a%'))\
                                     .order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))

    engine.dispose()

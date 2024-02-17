#!/usr/bin/python3
""" this script adds a state to the states table """

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )

    # Create a new State object with the desired name
    new_state = State(name="Louisiana")

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add the new state object to the session
    session.add(new_state)

    # Commit the transaction to the database
    session.commit()

    # Print the ID of the newly added state
    print(new_state.id)

    # Close the session and dispose of the engine
    session.close()
    engine.dispose()


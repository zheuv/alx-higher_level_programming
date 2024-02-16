#!/usr/bin/python3
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
Session = sessionmaker(bind=engine)
session = Session
for state in session.query(State).order_by(State.id):
    print("{} : {}".format(state.id, state.name))

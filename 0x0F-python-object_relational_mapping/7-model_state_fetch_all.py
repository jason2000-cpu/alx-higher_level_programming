#!/usr/bin/python3
"""
Write a script that lists all State objects from
the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine(
        'mysql://{}:{}@localhost:3306/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3],))
    Session = sessionmaker(bind=engine)
    Session = Session()

    states = Session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

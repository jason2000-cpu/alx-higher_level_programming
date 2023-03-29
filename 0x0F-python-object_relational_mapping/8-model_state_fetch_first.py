#!/usr/bin/python3
"""
This script prints the first 'State' object from the database
'hbtn_0e_4_usa'
"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3],))
    Session = sessionmaker(bind=engine)
    Session = Session()

    for state in Session.query(State).filter(State.id == 1):
        print('1: {}'.format(state.name))

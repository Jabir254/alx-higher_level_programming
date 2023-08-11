#!/usr/bin/python3
"""
lists all State objects that contain the letter a from the database
hbtn_0e_6_usa
take 3 arguments: mysql username, mysql password and database name
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    # Check command line arguments
    if len(sys.argv) != 4:
        print('Usage: {} username password database'.format(sys.argv[0]))
        sys.exit(1)

    # Create engine and session
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, database),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database
    query = session.query(State).filter(State.name.like('%a%')).\
        order_by(State.id)
    for state in query:
        print('{}: {}'.format(state.id, state.name))

    session.close()

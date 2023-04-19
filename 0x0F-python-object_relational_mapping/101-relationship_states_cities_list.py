#!/usr/bin/python3
"""
Lists all State objects and their corresponding\
City objects in the hbtn_0e_101_usa database.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City


if __name__ == '__main__':
    # Get command-line arguments
    mysql_user = sys.argv[1]
    mysql_pwd = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine and bind it to sessionmaker
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(mysql_user, mysql_pwd, db_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    # Create session
    session = Session()

    # Query the database for all State objects and
    # their corresponding City objects
    states = session.query(State).order_by(State.id, City.id).all()

    # Print the results
    for state in states:
        print('{}: {}'.format(state.id, state.name))
        for city in state.cities:
            print('\t{}: {}'.format(city.id, city.name))

    # Close session
    session.close()

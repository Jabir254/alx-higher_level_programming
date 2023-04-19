#!/usr/bin/python3
"""
prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    # get arguments
    mysql_user = sys.argv[1]
    mysql_pwd = sys.argv[2]
    db_name = sys.argv[3]
    search_state = sys.argv[4]

    # create engine and connect to database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(mysql_user, mysql_pwd, db_name),
                           pool_pre_ping=True)
    # create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query database for state
    query = session.query(State).filter(State.name == search_state).first()

    if query:
        print(query.id)
    else:
        print('Not found')
    session.close()

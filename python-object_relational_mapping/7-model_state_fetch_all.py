#!/usr/bin/python3

"""
Lists all State objects from database, using SQLAlchemy
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":

    usr = sys.argv[1]
    pwd = sys.argv[2]
    dbs = sys.argv[3]

    connection = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(usr, pwd, dbs)

    engine = create_engine(connection)

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State).all()
    for r in results:
        print("{}: {}".format(state.id, state.name))

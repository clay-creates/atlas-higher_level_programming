#!/usr/bin/python3

"""
Prints all City objects using state and Foreign key link,
using SQLAlchemy
"""

from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":

    usr = sys.argv[1]
    pwd = sys.argv[2]
    dbs = sys.argv[3]
    host = "localhost"
    url = "mysql+mysqldb"

    connection = "{}://{}:{}@{}:3306/{}".format(url, usr, pwd, host, dbs)

    engine = create_engine(connection)

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State, City).filter(State.id == City.state_id).all()
    for state, city in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

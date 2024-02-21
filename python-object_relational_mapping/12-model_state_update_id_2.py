#!/usr/bin/python3

"""
Change name of state with id=2 to New Mexico, using SQLAlchemy
"""

from model_state import Base, State
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

    state_update = session.query(State).where(State.id == 2).first()
    state_update.name = "New Mexico"
    session.commit()

    print(state_update.id)

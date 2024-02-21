#!/usr/bin/python3

"""
Delete all State objects with a name containing 'a', using SQLAlchemy
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

    state_a_delete = session.query(State).filter(State.name.like('%a%')).all()
    for state in state_a_delete:
        session.delete(state_a_delete)

    session.commit()

    for state in state_a_delete:
        print(state.id)

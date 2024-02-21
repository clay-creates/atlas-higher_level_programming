#!/usr/bin/python3

"""
Prints State obj with name passed as arg, using SQLAlchemy
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":

    usr = sys.argv[1]
    pwd = sys.argv[2]
    dbs = sys.argv[3]
    searchname = sys.argv[4]
    host = "localhost"
    url = "mysql+mysqldb"

    connection = "{}://{}:{}@{}:3306/{}".format(url, usr, pwd, host, dbs)

    engine = create_engine(connection)

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State).where(State.name == searchname).one_or_none()
    if results is None:
        print("Not found")
    else:
        print(results.id)

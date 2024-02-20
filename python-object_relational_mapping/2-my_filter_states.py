#!/usr/bin/python3

"""
Display all values in states where name matches argument, uding MySQLdb
"""

import MySQLdb
import sys

if __name__ == "__main__":

    usr = sys.argv[1]
    pw = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host='localhost', user=usr, passwd=pw, db=database)

    cursor = db.cursor()
    query = """SELECT * FROM states
    WHERE name = '{}'
    ORDER BY states.id ASC""".format(sys.argv[4])

    cursor.execute(query)
    for r in cursor.fetchall():
        print(r)

    cursor.close()
    db.close()

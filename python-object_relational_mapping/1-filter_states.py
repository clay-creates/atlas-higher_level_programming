#!/usr/bin/python3

"""
List all states with name starting with N, using MySQLdb
"""

import MySQLdb
import sys

if __name__ == "__main__":

    usr = sys.argv[1]
    pw = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host='localhost', user=usr, passwd=pw, db=database)

    cursor = db.cursor()

    cursor.execute(
        """SELECT * FROM states 
        WHERE states.name 
        LIKE 'N%' 
        ORDER BY states.id ASC"""
        )

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()

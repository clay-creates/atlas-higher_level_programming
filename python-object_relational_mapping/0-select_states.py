#!/usr/bin/python3

"""
Script to list all states using MySQLdb
"""

import MySQLdb
import sys

if __name__ == "__main__":

    un = sys.argv[1]
    pw = sys.argv[2]
    base = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=un, passwd=pw, db=base)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()

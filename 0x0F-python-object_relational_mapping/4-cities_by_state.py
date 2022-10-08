#!/usr/bin/python3
"""
This Srcript lists all states from the
database hbtn_0e_0_usa
"""


import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
            user=sys.argv[1],
            port=3306,
            passwd=sys.argv[2],
            db=sys.argv[3],
            )

    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
            FROM cities
            INNER JOIN states
            ON cities.state_id = states.id
            ORDER BY cities.id ASC;""")

    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()

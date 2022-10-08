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
    cur.execute("""SELECT cities.name FROM cities
                 WHERE cities.state_id = (SELECT id from states
                 WHERE name = %s)
                 ORDER BY cities.id ASC;""", (sys.argv[4],))

    cities = cur.fetchall()

    print(", ".join([city[0] for city in cities]))

    cur.close()
    db.close()

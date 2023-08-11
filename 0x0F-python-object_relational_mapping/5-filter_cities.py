#!/usr/bin/python3
"""
Lists cities all the cities in a state.
Take for arguments username, password, database, state_name
"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password\
              database state_name".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name,\
                states.name FROM cities JOIN states ON\
                cities.state_id = states.id WHERE states.name=%s\
                ORDER BY cities.id ASC", (state_name,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()

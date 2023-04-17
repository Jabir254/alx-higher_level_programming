#!/usr/bin/python3
"""
Lists all arguments and displays all values in the states table
takes for arguments: <username>
<password><database>
must use the model: import MySQLdb
should connect to a server running on localhost at port 3306
"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password database state".format(sys.argv[0]))
        sys.exit(1)

        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state = sys.argv[4]

        db = MySQLdb.connect(host="localhost", port=3306, user=username,
                             passwd=password, db=database)
        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                    (state,))
        rows = cur.fetchall()
        for row in rows:
            if username == state:
                print(row)

        cur.close()
        db.close()

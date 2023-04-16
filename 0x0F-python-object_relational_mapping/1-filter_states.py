#!/usr/bin/python3
""" lists all states with a name starting with N (upper N)
 from the database hbtn_0e_0_usa
 Usage: ./1-filter_states.py <mysql username>
                            <mysql password>
                            <database name>"""

import sys
from unicodedata import name
import MySQLdb

mysql_user = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]

# connect to MySQL server
conn = MySQLdb.connect(user=mysql_user, passwd=mysql_password,
       db=database_name)
# create a cursor object to execute SQL queries
cursor = conn.cursor()

# execute a SQL query to retrieve all states with a name starting with 'N'
cursor.execute("SELECT * FROM states WHERE name LIKE 'N%'")

# fetch all rows from the result set
rows = cursor.fetchall()

# print the rows
for row in rows:
    print(row)

# close cursor and database connection
cursor.close()
conn.close()

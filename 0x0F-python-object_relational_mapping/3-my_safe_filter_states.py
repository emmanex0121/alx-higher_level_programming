#!/usr/bin/python3

"""
    Takes arguments from user
    displays all values in the states table of database
    where name matches the input
    ENSURING THE SCRIPT IS SECURE FROM SQL INJECTION
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1], passwd=argv[2],
                         db=argv[3], host='localhost',
                         port=3306)

    cursor = db.cursor()

    user_input = argv[4]

    sql_query = "SELECT * FROM states\
                WHERE name LIKE BINARY %s\
                ORDER BY id ASC"

    cursor.execute(sql_query, (user_input, ))

    data = cursor.fetchall()

    for row in data:
        print(row)

    cursor.close()
    db.close()

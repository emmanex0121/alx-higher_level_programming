#!/usr/bin/python3

"""
    Takes in argument
    Displays all values in the states table of Database
    Where name matches argument
"""

from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1], passwd=argv[2],
                         db=argv[3],
                         host='localhost', port=3306)

    cursor = db.cursor()

    user_input = argv[4]

    query = "SELECT * FROM states\
            WHERE name = %s\
            ORDER BY id ASC"

    cursor.execute(query, (user_input,))

    data = cursor.fetchall()

    for row in data:
        print(row)

    cursor.close()
    db.close()

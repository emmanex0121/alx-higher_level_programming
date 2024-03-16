#!/usr/bin/python3

"""
    Lists all states with a name starting with Upper case N
    in the database
"""

from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2], db=argv[3],
                         host='localhost', port=3306)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states\
                    WHERE name LIKE 'N%'\
                    ORDER BY id ASC")

    data = cursor.fetchall()

    for row in data:
        print(row)

    cursor.close()
    db.close()

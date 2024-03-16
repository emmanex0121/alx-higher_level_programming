#!/usr/bin/python3

"""
    This Script lists all states from database hbtn_0e_0_usa
    Username Password and Database are provided as arguments respectively
"""

import sys
import MySQLdb

if __name__ == '__main__':
    MySQLdb.connect(user=sys.argv[1],
                    passwd=sys.argv[2], db=sys.argv[3],
                    host='localhost', port=3306)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    data = cursor.fetchall()

    for row in data:
        print(row)

    cursor.close()
    db.close()

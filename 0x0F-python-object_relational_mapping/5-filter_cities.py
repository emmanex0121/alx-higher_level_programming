#!/usr/bin/python3

"""
    Lists all cities from a state specified by user input
    from the database
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1], passwd=argv[2],
                         db=argv[3], host='localhost',
                         port=3306)

    cursor = db.cursor()

    sql_query = """SELECT cities.name FROM states
                INNER JOIN cities ON states.id = cities.state_id
                WHERE states.name = %s
                ORDER BY cities.id ASC"""

    cursor.execute(sql_query, (argv[4],))

    data = cursor.fetchall()

    print(", ".join([city[0] for city in data]))

    cursor.close()
    db.close()

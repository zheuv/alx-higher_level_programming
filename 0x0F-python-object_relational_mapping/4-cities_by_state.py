#!/usr/bin/python3
""" a Python script that lists the cities and their
states in the hbtn_0e_0_usa db """

if __name__ == "__main__":
    import MySQLdb
    import sys

    connection = MySQLdb.connect(
            host="localhost", port=3306,
            user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = connection.cursor()
    cur.execute(
            "SELECT cities.id, cities.name, states.name FROM cities "
            "JOIN states ON cities.state_id = states.id "
            "ORDER BY cities.id")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    connection.close()

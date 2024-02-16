#!/usr/bin/python3
""" a Python script that lists the states in the hbtn_0e_0_usa db """

if __name__ == "__main__":
    import MySQLdb
    import sys

    connection = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = connection.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    connection.close()

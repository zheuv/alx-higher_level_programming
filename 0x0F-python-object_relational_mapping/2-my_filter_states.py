#!/usr/bin/python3
""" a python script that lists the states starting with N in ascending order
    from the hbtn_0e_0_usa db """
if __name__ == "__main__":
    import MySQLdb as db
    import sys

    connection = db.connect(
        host="localhost", port=3306,
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = connection.cursor()
    cur.execute(
        f"SELECT * FROM states WHERE "
        f"states.name = '{sys.argv[4]}' ORDER BY states.id")
    rows = cur.fetchall()

    for row in rows:
        print(row)
    cur.close()
    connection.close()

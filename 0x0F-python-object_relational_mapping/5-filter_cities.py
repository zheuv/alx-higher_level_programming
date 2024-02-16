#!/usr/bin/python3
""" A Python script that lists the cities in the hbtn_0e_0_usa db """

if __name__ == "__main__":
    import MySQLdb
    import sys

    # Establish connection to the database
    connection = MySQLdb.connect(
        host="localhost", port=3306,
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3]
    )
    cur = connection.cursor()

    # Execute SQL query to select cities
    cur.execute(
        "SELECT cities.name FROM cities "
        "JOIN (SELECT states.id AS idd FROM "
        "states WHERE states.name LIKE BINARY %s) AS f "
        "ON cities.state_id = f.idd", (sys.argv[4],)
    )
    rows = cur.fetchall()

    # Concatenate city names into a single string separated by commas
    city_names = ', '.join(row[0] for row in rows)

    # Print the concatenated city names
    print(city_names)

    # Close cursor and connection
    cur.close()
    connection.close()

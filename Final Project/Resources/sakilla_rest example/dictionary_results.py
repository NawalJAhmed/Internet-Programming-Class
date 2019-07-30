

# import sqlite3
from utility.db import getConnection

# conn = sqlite3.connect("sqlite-sakila.sq")
#
# def dictionary_factory(cursor, row):
#     """
#     Create a dictionary from rows in a cursor result.
#     The keys will be the column names.
#     :param cursor: A cursor from which a query row has just been fetched
#     :param row: The query row that was fetched
#     :return: A dictionary associating column names to values
#     """
#     col_names = [d[0].lower() for d in cursor.description]
#     return dict(zip(col_names, row))
#
# conn.row_factory = dictionary_factory  # note: no parentheses

try:
    # crs = conn.cursor()
    conn = getConnection()
    crs = conn.cursor()
    cmd = "select * from actor"
    crs.execute(cmd)

    print(crs.description)

    for row in crs:
        print(row)


finally:
    conn.close()



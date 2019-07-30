

import sqlite3

conn = sqlite3.connect("sqlite-sakila.sq")

try:
    crs = conn.cursor()
    cmd = "select * from actor"
    crs.execute(cmd)

    for row in crs:
        print(row)

    print("=" * 40)

    for row in crs:
        print(row)


    crs.execute(cmd)
    actor_list = crs.fetchall()

    print("=" * 40)
    for row in actor_list:
        print(row)


    print("=" * 40)
    for row in actor_list:
        print(row)



finally:
    conn.close()



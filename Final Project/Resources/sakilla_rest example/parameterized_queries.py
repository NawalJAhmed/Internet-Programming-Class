


import sqlite3

conn = sqlite3.connect("sqlite-sakila.sq")

try:
    aid = 15
    crs = conn.cursor()
    cmd = "select * from actor where actor_id = "

    cmd1 = cmd + str(aid)
    crs.execute(cmd1)
    for row in crs :
        print(row)

    cmd = "select * from actor where actor_id = ?"
    crs.execute(cmd, (aid,))
    for row in crs :
        print(row)




finally:
    conn.close()


#  " select * from students where name = '" + name_entered + "'"

#  select * from students where name = 'Robert'; drop table students; -- '
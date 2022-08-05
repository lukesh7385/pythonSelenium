# insert ,update, delete
insert_query = "insert into student values(1, 'janvi','math')"
update_query = "update student set id=2 where name='janvi' "
delete_query = "delete from student where id=2"

import psycopg2

try:
    con = psycopg2.connect(host="localhost", port="5050", user="postgres", password="system", database="empinfo")
    curs = con.cursor()  # create cursor
    curs.execute(delete_query)
    con.commit()  # commit transaction
    con.close()
except:
    print("Connection is unsuccessful......")

print("finished......")

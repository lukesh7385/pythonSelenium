# insert ,update, delete
# select_query = "selcet * from student"


import psycopg2

try:
    con = psycopg2.connect(host="localhost", port="5050", user="postgres", password="system", database="empinfo")
    curs = con.cursor()  # create cursor
    curs.execute("select * from student")

    for row in curs:
        print(row[0], row[1], row[2])

    con.close()  # closed connection
except:
    print("Connection is unsuccessful......")

print("finished......")

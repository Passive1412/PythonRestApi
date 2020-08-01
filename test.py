import sqlite3
import os

connection = sqlite3.connect('data.db')

cursor = connection.cursor()
#if not os.path.exists('/home/marcus/projects/PythonRestApi/data.db'):
create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

user = (1, 'jose', 'asdf')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)


users = [
    (2, 'rolf', 'asdf'),
    (3, 'anne', 'xyz')
]

cursor.executemany(insert_query, users)

select_querry = "SELECT * FROM users"
for row in cursor.execute(select_querry):
    print(row)

connection.commit()

connection.close()
import sqlite3
conn = sqlite3.connect("users_db.db")

create_query = "CREATE TABLE users (user_name TEXT, user_password TEXT)"


users = [
    ('jack123', 'fafa0gh'),
    ('janepretty44', 'fasdafa0gh'),
    ('bobman123', 'f444dafa0gh')

]


insert_query = "INSERT INTO users VALUES (?, ?)"


cursor = conn.cursor()

cursor.executemany(insert_query, users)

conn.commit()

conn.close()
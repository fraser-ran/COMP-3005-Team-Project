import sqlite3
from sqlite3 import Error

print('starting database.py')
#! This only to make the database once after that we will need to make our commands in another file
# ? this means that if there is a db file in SQL, THIS WILL NOT RUN

cnn = None
fileName = 'SQL/books.db'

try:
    with open('SQL/ddl.sql', 'r') as sql_file:
        sql  = sql_file.read()
    cnn = sqlite3.connect(fileName)
    print('connected to database...')
    cs = cnn.cursor()
    # ! we only need to make the db once we will need to make our commands in another file 
    cs.executescript(sql)
    cnn.commit()
    cs.execute(sql)
    rst = cs.fetchall()
    print(rst)
except Error as e:
    print()
finally:
    if cnn:
        cnn.close()
    print('done...')



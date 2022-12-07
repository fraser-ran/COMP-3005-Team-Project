import sqlite3
from sqlite3 import Error

from sqlFunc import *


cnn = None
fileName = 'SQL/books.db'


try:
    cnn = sqlite3.connect(fileName)
    # sql = "" # ? here is where we would make our sql commands
    cs = cnn.cursor()
    # ? the execute method is used to run sql commands we need to have the 'sql' variable set to the command we want to run
    # cs.execute(sql)

except Error as e:
    print("error")
    print(e)
finally:
    if cnn:
        cnn.close()
    print('done...')


#examples of stuff TODO:
# try: 
#     cnn = sqlite3.connect('SQL/books.db')
#     sql = ("CREATE TABLE IF NOT EXISTS Book ("
#     "    isbn int,"
#     "    title varchar(255),"
#     "    publisher varchar(255),"
#     "    author_name varchar(255),"
#     "    genre varchar(255),"
#     "    num_pages int,"
#     "    price int,"
#     "    PRIMARY KEY(isbn))")
#     cs = cnn.cursor()
#     cs.execute(sql)
#     print('table created...')

#     sql = "select * from Book;"
#     cs.execute(sql)
#     rst = cs.fetchall()
#     print(rst)
# except Error as e:
#     print(e)
# finally:
#     if cnn:
#         cnn.close()
# print('done...')
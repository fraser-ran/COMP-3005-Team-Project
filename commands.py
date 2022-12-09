import sqlite3
from sqlite3 import Error

from sqlFunc import *

# for making changes to tables

cnn = None
fileName = 'SQL/books.db'


try:
    cnn = sqlite3.connect(fileName)
    sql = "ALTER TABLE Book ADD quantity INT;" # ? here is where we would make our sql commands
    cs = cnn.cursor()
    cs.executescript(sql)
    cnn.commit()
    cs.execute(sql)

    # ? the execute method is used to run sql commands we need to have the 'sql' variable set to the command we want to run
    cs.execute(sql)

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
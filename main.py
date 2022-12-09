import sqlite3
from sqlite3 import Error

from sqlFunc import *






if __name__ == "__main__":
    # addPublisher(1, "test Publisher", "test address","emai", "number","1234")
    insertBook(1, "title","test Publisher", "author", "action", 200, 20)
    print(searchLikeName('ti'))
    print(getPriceIsbn(2))
    pass



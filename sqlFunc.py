import sqlite3
from sqlite3 import Error


def insertBook(isbn, title, publisher, author_name, genre, num_pages, price):
    cnn = None
    fileName = 'SQL/books.db'
    try:
        cnn = sqlite3.connect(fileName)
        sql = ("INSERT INTO Book (isbn, title, publisher, author_name, genre, num_pages, price) VALUES (?, ?, ?, ?, ?, ?, ?)")
        cs = cnn.cursor()
        cs.execute(sql, (isbn, title, publisher, author_name, genre, num_pages, price))
        cnn.commit()
        print('book added...')
        sql = "select * from Book;"
        cs.execute(sql)
        rst = cs.fetchall()
        print(rst)
    except Error as e:
        print("error")
        print(e)
    finally:
        if cnn:
            cnn.close()
        print('done...')

def deleteBook(isbn):
    cnn = None
    fileName = 'SQL/books.db'
    try:
        cnn = sqlite3.connect(fileName)
        sql = ("DELETE FROM Book WHERE isbn = ?")
        cs = cnn.cursor()
        cs.execute(sql, (isbn,))
        cnn.commit()
        print('book deleted...')
    except Error as e:
        print("error")
        print(e)
    finally:
        if cnn:
            cnn.close()
        print('done...')
    
def updateBook(isbn, title, publisher, author_name, genre, num_pages, price):
    cnn = None
    fileName = 'SQL/books.db'
    try:
        cnn = sqlite3.connect(fileName)
        sql = ("UPDATE Book SET title = ?, publisher = ?, author_name = ?, genre = ?, num_pages = ?, price = ? WHERE isbn = ?")
        cs = cnn.cursor()
        cs.execute(sql, (title, publisher, author_name, genre, num_pages, price, isbn))
        cnn.commit()
        print('book updated...')
    except Error as e:
        print("error")
        print(e)
    finally:
        if cnn:
            cnn.close()
        print('done...')

def searchBook(value, browseBy):
    cnn = None
    fileName = 'SQL/books.db'
    try:
        cnn = sqlite3.connect(fileName)
        sql = ("SELECT * FROM Book WHERE "+browseBy+" = ?")
        cs = cnn.cursor()
        cs.execute(sql, (value,))
        rst = cs.fetchall()
        return rst
    except Error as e:
        print("error")
        print(e)
    finally:
        if cnn:
            cnn.close()
        print('done...')

def searchBookByTitle(title):
    cnn = None
    fileName = 'SQL/books.db'
    try:
        cnn = sqlite3.connect(fileName)
        sql = ("SELECT * FROM Book WHERE title = ?")
        cs = cnn.cursor()
        cs.execute(sql, (title,))
        rst = cs.fetchall()
        print(rst)
    except Error as e:
        print("error")
        print(e)
    finally:
        if cnn:
            cnn.close()
        print('done...')

def searchBookByAuthor(author_name):
    cnn = None
    fileName = 'SQL/books.db'
    try:
        cnn = sqlite3.connect(fileName)
        sql = ("SELECT * FROM Book WHERE author_name = ?")
        cs = cnn.cursor()
        cs.execute(sql, (author_name,))
        rst = cs.fetchall()
        print(rst)
    except Error as e:
        print("error")
        print(e)
    finally:
        if cnn:
            cnn.close()
        print('done...')

def searchBookByGenre(genre):
    cnn = None
    fileName = 'SQL/books.db'
    try:
        cnn = sqlite3.connect(fileName)
        sql = ("SELECT * FROM Book WHERE genre = ?")
        cs = cnn.cursor()
        cs.execute(sql, (genre,))
        rst = cs.fetchall()
        print(rst)
    except Error as e:
        print("error")
        print(e)
    finally:
        if cnn:
            cnn.close()
        print('done...')

def searchBookByPublisher(publisher):
    cnn = None
    fileName = 'SQL/books.db'
    try:
        cnn = sqlite3.connect(fileName)
        sql = ("SELECT * FROM Book WHERE publisher = ?")
        cs = cnn.cursor()
        cs.execute(sql, (publisher,))
        rst = cs.fetchall()
        print(rst)
    except Error as e:
        print("error")
        print(e)
    finally:
        if cnn:
            cnn.close()
        print('done...')

def searchBookByPrice(price):
    cnn = None
    fileName = 'SQL/books.db'
    try:
        cnn = sqlite3.connect(fileName)
        sql = ("SELECT * FROM Book WHERE price = ?")
        cs = cnn.cursor()
        cs.execute(sql, (price,))
        rst = cs.fetchall()
        print(rst)
    except Error as e:
        print("error")
        print(e)
    finally:
        if cnn:
            cnn.close()
        print('done...')

def searchBookByNumPages(num_pages):
    cnn = None
    fileName = 'SQL/books.db'
    try:
        cnn = sqlite3.connect(fileName)
        sql = ("SELECT * FROM Book WHERE num_pages = ?")
        cs = cnn.cursor()
        cs.execute(sql, (num_pages,))
        rst = cs.fetchall()
        print(rst)
    except Error as e:
        print("error")
        print(e)
    finally:
        if cnn:
            cnn.close()
        print('done...')

def searchBookByPriceRange(min, max):
    cnn = None
    fileName = 'SQL/books.db'
    try:
        cnn = sqlite3.connect(fileName)
        sql = ("SELECT * FROM Book WHERE price BETWEEN ? AND ?")
        cs = cnn.cursor()
        cs.execute(sql, (min, max))
        rst = cs.fetchall()
        print(rst)
    except Error as e:
        print("error")
        print(e)
    finally:
        if cnn:
            cnn.close()
        print('done...')

def displayBooks():
    cnn = None
    fileName = 'SQL/books.db'
    try:
        cnn = sqlite3.connect(fileName)
        sql = ("SELECT * FROM Book")
        cs = cnn.cursor()
        cs.execute(sql)
        rst = cs.fetchall()
        print(rst)
    except Error as e:
        print("error")
        print(e)
    finally:
        if cnn:
            cnn.close()
        print('done...')

#@ param addCustomer (int, varchar, varchar, varchar, varchar, varchar, varchar, varchar, varchar, int, int, Date, varchar, varchar, varchar)
def addCustomer(u_id, userName, email, password, address, country, city, postalCode, cardName, cardNumber, ccv, exp_Date, billingStreet, billingCity, billingCountry):

    cnn = None
    fileName = 'SQL/books.db'
    try:
        cnn = sqlite3.connect(fileName)
        sql = ("INSERT INTO Customer(u_id, userName, email, password, address, country, city, postalCode, cardName, cardNumber, ccv, exp_Date, billingStreet, billingCity, billingCountry) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)")
        cs = cnn.cursor()
        cs.execute(sql, (u_id, userName, email, password, address, country, city, postalCode, cardName, cardNumber, ccv, exp_Date, billingStreet, billingCity, billingCountry))
        cnn.commit()
        print('customer added...')
    except Error as e:
        print("error")
        print(e)
    finally:
        if cnn:
            cnn.close()
        print('done...')

def searchCustomerByUserName(userName):
    cnn = None
    fileName = 'SQL/books.db'
    try:
        cnn = sqlite3.connect(fileName)
        sql = ("SELECT * FROM Customer WHERE userName = ?")
        cs = cnn.cursor()
        cs.execute(sql, (userName,))
        rst = cs.fetchall()
        print(rst)
    except Error as e:
        print("error")
        print(e)
    finally:
        if cnn:
            cnn.close()
        print('done...')

def searchCustomerByEmail(email):
    cnn = None
    fileName = 'SQL/books.db'
    try:
        cnn = sqlite3.connect(fileName)
        sql = ("SELECT * FROM Customer WHERE email = ?")
        cs = cnn.cursor()
        cs.execute(sql, (email,))
        rst = cs.fetchall()
        print(rst)
    except Error as e:
        print("error")
        print(e)
    finally:
        if cnn:
            cnn.close()
        print('done...')

def addPublisher(p_id, name, address, email, phoneNum, bankAccount):
    cnn = None
    fileName = 'SQL/books.db'
    try:
        cnn = sqlite3.connect(fileName)
        sql = ("INSERT INTO Publisher(p_id, name, address, email, phoneNum, bankAccount) VALUES(?, ?, ?, ?, ?, ?)")
        cs = cnn.cursor()
        cs.execute(sql, (p_id, name, address, email, phoneNum, bankAccount))
        cnn.commit()
        print('publisher added...')
    except Error as e:
        print("error")
        print(e)
    finally:
        if cnn:
            cnn.close()
        print('done...')


def searchPublisherByName(name):
    cnn = None
    fileName = 'SQL/books.db'
    try:
        cnn = sqlite3.connect(fileName)
        sql = ("SELECT * FROM Publisher WHERE name = ?")
        cs = cnn.cursor()
        cs.execute(sql, (name,))
        rst = cs.fetchall()
        print(rst)
    except Error as e:
        print("error")
        print(e)
    finally:
        if cnn:
            cnn.close()
        print('done...')

def searchPublisherByEmail(email):
    cnn = None
    fileName = 'SQL/books.db'
    try:
        cnn = sqlite3.connect(fileName)
        sql = ("SELECT * FROM Publisher WHERE email = ?")
        cs = cnn.cursor()
        cs.execute(sql, (email,))
        rst = cs.fetchall()
        print(rst)
    except Error as e:
        print("error")
        print(e)
    finally:
        if cnn:
            cnn.close()
        print('done...')

def searchLikeName(likeName):

    cnn = None
    fileName = 'SQL/books.db'
    try:
        cnn = sqlite3.connect(fileName)
        line = ("SELECT * FROM Book WHERE title LIKE " + "'%" + likeName + "%'")
        sql = line
        cs = cnn.cursor()
        cs.execute(sql)
        rst = cs.fetchall()
        print(rst)
    except Error as e:
        print("error")
        print(e)
    finally:
        if cnn:
            cnn.close()
        print('done...')

def searchLikeAuthor(likeAuthor):

    cnn = None
    fileName = 'SQL/books.db'
    try:
        cnn = sqlite3.connect(fileName)
        line = ("SELECT * FROM Book WHERE author LIKE " + "'%" + likeAuthor + "%'")
        sql = line
        cs = cnn.cursor()
        cs.execute(sql)
        rst = cs.fetchall()
        print(rst)
    except Error as e:
        print("error")
        print(e)
    finally:
        if cnn:
            cnn.close()
        print('done...')

def searchLikeGenre(likeGenre):
    
        cnn = None
        fileName = 'SQL/books.db'
        try:
            cnn = sqlite3.connect(fileName)
            line = ("SELECT * FROM Book WHERE genre LIKE " + "'%" + likeGenre + "%'")
            sql = line
            cs = cnn.cursor()
            cs.execute(sql)
            rst = cs.fetchall()
            print(rst)
        except Error as e:
            print("error")
            print(e)
        finally:
            if cnn:
                cnn.close()
            print('done...')


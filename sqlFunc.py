import sqlite3
from sqlite3 import Error


def insertBook(isbn, title, publisher, author_name, genre, num_pages, price, quantity):
    cnn = None
    fileName = 'SQL/books.db'
    try:
        cnn = sqlite3.connect(fileName)
        sql = ("INSERT INTO Book (isbn, title, publisher, author_name, genre, num_pages, price, quantity) VALUES (?, ?, ?, ?, ?, ?, ?, ?)")
        cs = cnn.cursor()
        cs.execute(sql, (isbn, title, publisher, author_name, genre, num_pages, price, quantity))
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
    
def updateBook(isbn, title, publisher, author_name, genre, num_pages, price, quantity):
    cnn = None
    fileName = 'SQL/books.db'
    try:
        cnn = sqlite3.connect(fileName)
        sql = ("UPDATE Book SET title = ?, publisher = ?, author_name = ?, genre = ?, num_pages = ?, price = ?, quantity = ? WHERE isbn = ?")
        cs = cnn.cursor()
        cs.execute(sql, (title, publisher, author_name, genre, num_pages, price,quantity, isbn))
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
def addCustomer(u_id, username, email, password, address, country, city, postalCode, cardName, cardNumber, ccv, exp_Date, billingStreet, billingCity, billingCountry):

    cnn = None
    fileName = 'SQL/books.db'
    try:
        cnn = sqlite3.connect(fileName)
        sql = ("INSERT INTO Users(u_id, username, email, password, address, country, city, postal_code, card_name, card_number, ccv, exp_Date, billing_street, billing_city, billing_country) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)")
        cs = cnn.cursor()
        cs.execute(sql, (u_id, username, email, password, address, country, city, postalCode, cardName, cardNumber, ccv, exp_Date, billingStreet, billingCity, billingCountry))
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
        sql = ("SELECT * FROM Users WHERE username = ?")
        cs = cnn.cursor()
        cs.execute(sql, (userName,))
        rst = cs.fetchall()
        return rst
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
        sql = ("SELECT * FROM Users WHERE email = ?")
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

def addPublisher(p_id, name, address, email, phone_num, bankAccount):
    cnn = None
    fileName = 'SQL/books.db'
    print("in add publisher")
    try:
        cnn = sqlite3.connect(fileName)
        sql = ("INSERT INTO Publisher(p_id, name, address, email, phone_number, bank_account) VALUES(?, ?, ?, ?, ?, ?)")
        cs = cnn.cursor()
        cs.execute(sql, (p_id, name, address, email, phone_num, bankAccount))
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
        return rst
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
        line = ("SELECT * FROM Book WHERE author_name LIKE " + "'%" + likeAuthor + "%'")
        sql = line
        cs = cnn.cursor()
        cs.execute(sql)
        rst = cs.fetchall()
        return rst
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
            return rst
        except Error as e:
            print("error")
            print(e)
        finally:
            if cnn:
                cnn.close()
            print('done...')

def getPriceIsbn(isbn):
    cnn = None
    fileName = 'SQL/books.db'
    price =0
    try:
        cnn = sqlite3.connect(fileName)
        sql = ("SELECT price FROM Book WHERE isbn = ?")
        cs = cnn.cursor()
        cs.execute(sql, (isbn,))
        rst = cs.fetchall()
        # print(rst)
        price = rst[0][0]
    except Error as e:
        print("error")
        print(e)
    finally:
        if cnn:
            cnn.close()
        print('done...')
    return price

def getListPricesIsbn(isbnList):
    cnn = None
    fileName = 'SQL/books.db'
    price =0
    priceList = []
    try:
        cnn = sqlite3.connect(fileName)
        sql = ("SELECT price FROM Book WHERE isbn = ?")
        cs = cnn.cursor()
        for isbn in isbnList:
            cs.execute(sql, (isbn,))
            rst = cs.fetchall()
            # print(rst)
            price = rst[0][0]
            priceList.append(price)
    except Error as e:
        print("error")
        print(e)
    finally:
        if cnn:
            cnn.close()
        print('done...')
    return priceList

def addToOrder(o_id, u_id, cost):
    cnn = None
    fileName = 'SQL/books.db'
    try:
        cnn = sqlite3.connect(fileName)
        sql = ("INSERT INTO Orders(o_id, u_id, date, time, cost) VALUES(?, ?, CURRENT_DATE, CURRENT_TIME, ?)")
        cs = cnn.cursor()
        cs.execute(sql, (o_id, u_id, cost))
        cnn.commit()
        print('order added...')
    except Error as e:
        print("error")
        print(e)
    finally:
        if cnn:
            cnn.close()
        print('done...')

def checkIfCardisNull(name):
    cnn = None
    fileName = 'SQL/books.db'
    try:
        cnn = sqlite3.connect(fileName)
        sql = ("SELECT * FROM Users WHERE card_number IS NULL and username = ?")
        cs = cnn.cursor()
        cs.execute(sql, (name,))
        rst = cs.fetchall()
        return rst  
    except Error as e:
        print("error")
        print(e)
    finally:
        if cnn:
            cnn.close()
        print('done...')

def updateCardInfo(cardNumber, cardName, cardExp, cardCcv, billingStreet, billingCity , billingCountry, username):
    cnn = None
    fileName = 'SQL/books.db'
    try:
        cnn = sqlite3.connect(fileName)
        sql = ("UPDATE Users SET card_number = ?, card_name = ?, exp_date = ?, ccv = ?, billing_street = ?, billing_city = ?, billing_country = ? WHERE username = ?")
        cs = cnn.cursor()
        cs.execute(sql, (cardNumber, cardName, cardExp, cardCcv, billingStreet, billingCity , billingCountry, username))
        cnn.commit()
        print('card info updated...')
        return True
    except Error as e:
        print("error")
        print(e)
        return False
    finally:
        if cnn:
            cnn.close()
        print('done...')

def updateQuantity(isbn, quantity):
    cnn = None
    fileName = 'SQL/books.db'
    try:
        cnn = sqlite3.connect(fileName)
        sql = ("UPDATE Book SET quantity = ? WHERE isbn = ?")
        cs = cnn.cursor()
        cs.execute(sql, (quantity, isbn))
        cnn.commit()
        print('quantity updated...')
    except Error as e:
        print("error")
        print(e)
    finally:
        if cnn:
            cnn.close()
        print('done...')

def getOrderCount():
    cnn = None
    fileName = 'SQL/books.db'
    try:
        cnn = sqlite3.connect(fileName)
        sql = ("SELECT COUNT(*) FROM Orders")
        cs = cnn.cursor()
        cs.execute(sql)
        rst = cs.fetchall()
        return rst  
    except Error as e:
        print("error")
        print(e)
    finally:
        if cnn:
            cnn.close()
        print('done...')

def getOrders():
    cnn = None
    fileName = 'SQL/books.db'
    try:
        cnn = sqlite3.connect(fileName)
        sql = ("SELECT * FROM Orders")
        cs = cnn.cursor()
        cs.execute(sql)
        rst = cs.fetchall()
        return rst  
    except Error as e:
        print("error")
        print(e)
    finally:
        if cnn:
            cnn.close()
        print('done...')

def getSalesByIsbn(isbn):
    cnn = None
    fileName = 'SQL/books.db'
    try:
        cnn = sqlite3.connect(fileName)
        sql = ("SELECT * FROM Sales WHERE isbn = ?")
        cs = cnn.cursor()
        cs.execute(sql, (isbn,))
        rst = cs.fetchall()
        return rst  
    except Error as e:
        print("error")
        print(e)
    finally:
        if cnn:
            cnn.close()
        print('done...')

def checkSaleEmpty(isbn):
    cnn = None
    fileName = 'SQL/books.db'
    try:
        cnn = sqlite3.connect(fileName)
        sql = ("SELECT * FROM Sales WHERE isbn = ?")
        cs = cnn.cursor()
        cs.execute(sql, (isbn,))
        rst = cs.fetchall()
        if len(rst) == 0:
            return True
        else:
            return False
    except Error as e:
        print("error")
        print(e)
    finally:
        if cnn:
            cnn.close()
        print('done...')

def makeSale(isbn, cost):
    cnn = None
    fileName = 'SQL/books.db'
    try:
        if (checkSaleEmpty(isbn)):
            cnn = sqlite3.connect(fileName)
            sql = ("INSERT INTO Sales(isbn, title, publisher, cost, num_sold, profits) VALUES(?, ?, ?, ?, ?, ?)")
            cs = cnn.cursor()
            cs.execute(sql, (isbn, cost, 1, cost*1))
            cnn.commit()
            print('sale added...')
        
        else:
            cnn = sqlite3.connect(fileName)
            sql = ("UPDATE Sales SET num_sold = num_sold + 1, profits = (num_sold+1)*cost WHERE isbn = ?")
            cs = cnn.cursor()
            cs.execute(sql, (isbn,))
            cnn.commit()
            print('sale updated...')
    except Error as e:
        print("error")
        print(e)
    finally:
        if cnn:
            cnn.close()
        print('done...')

def returnProfits(value, searchBy):
    cnn = None
    fileName = 'SQL/books.db'
    try:
        cnn = sqlite3.connect(fileName)
        sql = ("SELECT SUM(profits), SUM(num_sold) FROM Sales INNER JOIN Book ON Sales.isbn = Book.isbn WHERE "+searchBy+" = ?")
        cs = cnn.cursor()
        cs.execute(sql, (value,))
        rst = cs.fetchall()
        print(rst[0])
        return rst[0]
    except Error as e:
        print("error")
        print(e)
    finally:
        if cnn:
            cnn.close()
        print('done...')

def searchOrder(id):
    cnn = None
    fileName = 'SQL/books.db'
    try:
        cnn = sqlite3.connect(fileName)
        sql = ("SELECT Users.username, Users.country, Users.city FROM Orders INNER JOIN Users ON Orders.u_id = Users.username WHERE o_id = ?")
        cs = cnn.cursor()
        cs.execute(sql, (id,))
        rst = cs.fetchall()
        print(rst)
        return rst
    except Error as e:
        print("error")
        print(e)
    finally:
        if cnn:
            cnn.close()
        print('done...')
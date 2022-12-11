import sqlite3
from sqlite3 import Error


def insertBook(isbn, title, publisher, author_name, genre, num_pages, price, quantity):
    """
    This function will insert a book into the database
    :param isbn: int
    :param title: string
    :param publisher: string
    :param author_name: string
    :param genre: string
    :param num_pages: int
    :param price: int
    :param quantity: int
    :return: None
    """
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
    """
    This function will delete a book from the database
    :param isbn: int
    :return: None
    """
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
    """
    This function will update a book in the database
    :param isbn: int
    :param title: string
    :param publisher: string
    :param author_name: string
    :param genre: string
    :param num_pages: int
    :param price: int
    :param quantity: int
    :return: None
    """
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
    """
    This function will search for a book in the database
    :param value: string
    :param browseBy: string
    :return: None
    """
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
    """
    This function will search for a book in the database
    :param title: string
    :return: None
    """
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
    """
    This function will search for a book in the database
    :param author_name: string
    :return: None
    """
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
    """
    This function will search for a book in the database
    :param genre: string
    :return: None
    """
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
    """
    This function will search for a book in the database
    :param publisher: string
    :return: None
    """
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
    """
    This function will search for a book in the database
    :param price: int
    :return: None
    """
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
    """
    This function will search for a book in the database
    :param num_pages: int
    :return: None
    """
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
    """
    This function will search for a book in the database
    :param min: int
    :param max: int
    :return: None
    """
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
    """
    This function will display all books in the database
    :return: None
    """
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
    """
    This function will add a customer to the database
    :param u_id: int
    :param username: varchar
    :param email: varchar
    :param password: varchar
    :param address: varchar
    :param country: varchar
    :param city: varchar
    :param postalCode: varchar
    :param cardName: varchar
    :param cardNumber: int
    :param ccv: int
    :param exp_Date: Date
    :param billingStreet: varchar
    :param billingCity: varchar
    :param billingCountry: varchar
    :return: None
    """
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
    """ This function will search for a customer in the database
    :param userName: varchar
    :return: None
    """
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
    """ This function will search for a customer in the database
    :param email: varchar
    :return: None
    """

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
    """ This function will add a publisher to the database
    :param p_id: int
    :param name: varchar
    :param address: varchar
    :param email: varchar
    :param phone_num: varchar
    :param bankAccount: varchar
    :return: None
    """
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
    """ 
    This function will search for a publisher in the database
    :param name: varchar
    :return: None
    """
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
    """
    This function will search for a publisher in the database
    :param email: varchar
    :return: None
    """

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
    """ This function will search for a book in the database
    :param likeName: varchar
    :return: None
    """

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
    """
    This function will search for a book in the database
    :param likeAuthor: varchar
    :return: None
    """
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
        """ 
        This function will search for a book in the database
        :param likeGenre: varchar
        :return: None
        """

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
    """ 
    This function will get the price of a book by isbn
    :param isbn: int
    :return: price tuple
    """
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
    """
    This function will get the price of a book by isbn
    :param isbn: int
    :return: price tuple list
    """
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
    """
    This function will add an order to the database
    :param o_id: int
    :param u_id: int
    :param cost: float
    :return: None
    """
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
    """     
    This function will check if the card info is null
    :param name: varchar
    :return: the Users info if the cardInfo is null
    """
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
    """
    This function will update the card info
    :param cardNumber: int
    :param cardName: varchar
    :param cardExp: varchar
    :param cardCcv: int
    :param billingStreet: varchar
    :param billingCity: varchar
    :param billingCountry: varchar
    :param username: varchar
    :return: true if card is updated false if not
    """
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
    """
    This function will update the quantity of a book
    :param isbn: int
    :param quantity: int
    :return: None
    """
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
    """
    This function will get the order count
    :return: order count
    """

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
    """ 
    This function will get all the orders
    :return: all the orders
    """
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
    """ 
    This function will get the sales by isbn
    :param isbn: int
    :return: the sales by isbn
    """
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
    """
    This function will check if the sale is empty
    :param isbn: int
    :return: true if empty false if not
    """

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
    """
    This function will make a sale if that book has not been sold before, but if so then 
    :param isbn: int
    :param cost: float
    :return: None
    """

    cnn = None
    fileName = 'SQL/books.db'
    try:
        if (checkSaleEmpty(isbn)):
            cnn = sqlite3.connect(fileName)
            sql = ("INSERT INTO Sales(isbn, cost, num_sold, profits) VALUES(?, ?, ?, ?)")
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
    """
    This function will return the profits and number of books sold
    :param value: string
    :param searchBy: string
    :return: the profits and number of books sold
    """
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
    """ 
    This function will get the Order by Order number
    :param isbn: Order ID
    :return: Order status
    """
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
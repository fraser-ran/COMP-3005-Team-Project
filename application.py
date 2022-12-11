from tkinter import *
from tkinter import ttk
import sqlite3
from sqlite3 import Error

from sqlFunc import *
from datetime import datetime, date

folderName = ""

#initalize window
window = Tk()
window.title("Book Store")
window.geometry("750x500")

#initialize current status of the user, being logged out with an empty cart
currentUser = []
signedIn = False
cart = []
totalBackup = 0


#initalize all GUI aspects of the application (Labels, Entry Text Boxes, Drop Down Menus, Buttons, Lists)
title = Label(window, text = "Welcome to the Bookstore")
title.config(font =("Arial", 14))
title.pack()
browseLabel = Label(window, text = "Browse by:")
browseLabel.config(font =("Arial", 12))
browseLabel.place(x=10,y=50)
drop = ttk.Combobox(
    state="readonly",
    values=["Title", "Author", "ISBN", "Genre", "Publisher","Keyword","Key-Author","Similar Genre"]
)
drop.set("ISBN")
drop.place(x=100,y=53)
box = Entry(width=50)
box.place(x=250,y=55)
list = Listbox(window, width=50,height=20)
list.place(x=250,y=100)
bookTitle = Label(window, text = "")
bookTitle.config(font =("Arial", 14))
isbnTitle = Label(window, text = "ISBN = ")
isbnTitle.config(font =("Arial", 12))
publisherTitle = Label(window, text = "Publisher = ")
publisherTitle.config(font =("Arial", 12))
authorTitle = Label(window, text = "Author = ")
authorTitle.config(font =("Arial", 12))
genreTitle = Label(window, text = "Genre = ")
genreTitle.config(font =("Arial", 12))
pageTitle = Label(window, text = "Number of Pages = ")
pageTitle.config(font =("Arial", 12))
priceTitle = Label(window, text = "Price = $")
priceTitle.config(font =("Arial", 12))  
stockTitle = Label(window, text = "Quantity = ")
stockTitle.config(font =("Arial", 12))
stockBox = Entry(width=10)
buyBtn = Button(window, text = 'Add to Cart', bd = '3',command=lambda: buyButton())
buyBtn.config(height=2,width=10)
editStockBtn = Button(window, text = 'Update Quantity', bd = '3',command=lambda: editStock())
editStockBtn.config(height=2,width=15)
deleteBtn = Button(window, text = 'Delete Book', bd = '3',command=lambda: removeBook())
deleteBtn.config(height=2,width=15)
orderTrackBtn = Button(window, text = 'Track Order', bd = '3',command=lambda: trackButton())
orderTrackBtn.place(x=10,y=80)
titleBox = Entry(width=50)
isbnBox = Entry(width=50)
publisherBox = Entry(width=50)
authorBox = Entry(width=50)
genreBox = Entry(width=50)
pageBox = Entry(width=50)
priceBox = Entry(width=50)
backBtn = Button(window, text = 'Back', bd = '3',command=lambda: backButton())
backBtn.config(height=1,width=5)
backBtn.place(x=685,y=10)  
btn = Button(window, text = 'Search', bd = '3',command=lambda: search())
btn.place(x=560,y=50)
reg = Button(window, text = 'Register', bd = '3',command=lambda: registerButton())
reg.place(x=10,y=10)
login = Button(window, text = 'Login', bd = '3',command=lambda: loginButton())
login.place(x=80,y=10)
logout = Button(window, text = 'Logout', bd = '3',command=lambda: logoutButton())
window.columnconfigure(0,weight=1)
emailBox = Entry(width=60)
usernameBox = Entry(width=50)
passwordBox = Entry(width=50)
cityBox = Entry(width=60)
addressBox = Entry(width=50)
postalBox = Entry(width=50)
signinBtn = Button(window, text = 'Sign In', bd = '3',command=lambda: signin())
signinBtn.config(height=2,width=10)
failedSignin = Label(window, bg="red", text = "Invalid Login Information")
failedSignin.config(font =("Arial", 12))
cartLabel = Label(window, bg="yellow", text = "Added to Cart")
cartLabel.config(font =("Arial", 12))
signupBtn = Button(window, text = 'Sign Up', bd = '3',command=lambda: signup(0))
signupBtn.config(height=2,width=10)
signupAdminBtn = Button(window, text = 'Sign Up as Admin', bd = '3',command=lambda: signup(1))
signupAdminBtn.config(height=2,width=20)
emailTitle = Label(window, text = "Email: ")
emailTitle.config(font =("Arial", 12))
usernameTitle = Label(window, text = "Username: ")
usernameTitle.config(font =("Arial", 12))
passwordTitle = Label(window, text = "Password: ")
passwordTitle.config(font =("Arial", 12))
countryTitle = Label(window, text = "Country: ")
countryTitle.config(font =("Arial", 12))
cityTitle = Label(window, text = "City: ")
cityTitle.config(font =("Arial", 12))
addressTitle = Label(window, text = "Address: ")
addressTitle.config(font =("Arial", 12))
postalTitle = Label(window, text = "Postal Code: ")
postalTitle.config(font =("Arial", 12))
countryDrop = ttk.Combobox(
    state="readonly",
    values=["Canada", "United States","Mexico"]
)
viewCartBtn = Button(window, text = 'View Cart', bd = '3',command=lambda: viewCart())
editBankBtn = Button(window, text = 'Edit Bank Info', bd = '3',command=lambda: editBankButton())
addBookBtn = Button(window, text = 'Add Book', bd = '3',command=lambda: addButton())
confirmAddBtn = Button(window, text = 'Add Book', bd = '3',command=lambda: addBookButton())
confirmAddBtn.config(height=2,width=10)
statsBtn = Button(window, text = 'View Stats', bd = '3',command=lambda: statsButton())
statsDrop = ttk.Combobox(
    state="readonly",
    values=["Title", "Author", "ISBN", "Genre", "Publisher"]
)
statsDrop.set("ISBN")
statsBox = Entry(width=50)
statsSearchBtn = Button(window, text = 'Search', bd = '3',command=lambda: searchStats())
profitLabel = Label(window, text = "Profit = $ ")
numSoldLabel = Label(window, text = "Copies Sold = ")
orderEntry = Entry(width=10)
trackLabel = Label(window, text = "Enter Order #: ")
trackResultLabel = Label(window, text = "")
trackBtn = Button(window, text = 'Track Order', bd = '3',command=lambda: trackOrder())
cartDisplay = Listbox(window, width=50,height=20)
totalTitle = Label(window, text = "Total = $ ")
checkoutBtn = Button(window, text = 'Check Out', bd = '3',command=lambda: checkoutButton())
checkoutTitle = Label(window, text = "Successfully Checked Out")
restockDisplay = Label()
cardNumBox = Entry(width=50)
cardNameBox = Entry(width=50)
cardExpDateBox1 = Entry(width=5)
cardExpDateBox2 = Entry(width=5)
cardCCVBox = Entry(width=50)
billstreetBox = Entry(width=50)
billcityBox = Entry(width=50)
billcountryDrop = ttk.Combobox(
    state="readonly",
    values=["Canada", "United States","Mexico"]
)
cardNumTitle = Label(window, text = "Card Number: ")
cardNumTitle.config(font =("Arial", 12))
cardNameTitle = Label(window, text = "Card Name: ")
cardNameTitle.config(font =("Arial", 12))
cardExpDateTitle = Label(window, text = "Expiry Date (YY/MM): ")
cardExpDateTitle.config(font =("Arial", 12))
cardCCVTitle = Label(window, text = "CCV: ")
cardCCVTitle.config(font =("Arial", 12))
billstreetTitle = Label(window, text = "Billing Street: ")
billstreetTitle.config(font =("Arial", 12))
billcityTitle = Label(window, text = "Billing City: ")
billcityTitle.config(font =("Arial", 12))
billcountryTitle = Label(window, text = "Billing Country: ")
billcountryTitle.config(font =("Arial", 12))
confirmEditBankBtn = Button(window, text = 'Confirm Changes', bd = '3',command=lambda: confirmEditBank())
confirmEditBankBtn.config(height=2,width=15)
checkoutTitle = Label(window, text = "Successfully Edited Bank Account")



def search():
    """
    search grabs the value from the drop down menu to determine what the user
    wants to search by, grabs the value to be queried from the search entry box, finds matching
    books that contain the value and display them on a list for the user 

    """ 
    #Search for book based on drop down menu
    if(drop.get().lower() == "author"):
        searchList = searchBook(box.get(), "author_name")
    
    elif(drop.get().lower() == "keyword"):
        searchList = searchLikeName(box.get())
    elif(drop.get().lower() == "key-author"):
        searchList = searchLikeAuthor(box.get())
    elif(drop.get().lower() == "similar genre"):
        searchList = searchLikeGenre(box.get())
    else:
        searchList = searchBook(box.get(), drop.get().lower())

    #Create List
    list.delete(0,END)
    for i in range(0,len(searchList)):
        list.insert(i,searchList[i])
        #print(searchList[i])


def select(event):
    """
    select loads a page for a selected book via a double click from the list

    :param event: double click event

    """ 
    global currentUser, signedIn
    print(currentUser)
    list.place_forget()
    drop.place_forget()
    btn.place_forget()
    box.place_forget()
    browseLabel.place_forget()
    title.pack_forget()
    bookTitle.config(text = list.get(ACTIVE)[1] ,font =("Arial", 14))
    isbnTitle.config(text = "ISBN = "+str(list.get(ACTIVE)[0]),font =("Arial", 12))
    publisherTitle.config(text = "Publisher = "+list.get(ACTIVE)[2],font =("Arial", 12))
    authorTitle.config(text = "Author = "+list.get(ACTIVE)[3],font =("Arial", 12))
    genreTitle.config(text = "Genre = "+list.get(ACTIVE)[4],font =("Arial", 12))
    pageTitle.config(text = "Number of Pages = "+str(list.get(ACTIVE)[5]),font =("Arial", 12))
    priceTitle.config(text = "Price = $"+str(list.get(ACTIVE)[6]),font =("Arial", 12))  
    
    bookTitle.pack()
    isbnTitle.place(x=250, y=50)
    publisherTitle.place(x=250, y=100)
    authorTitle.place(x=250, y=150)
    genreTitle.place(x=250, y=200)
    pageTitle.place(x=250, y=250)
    priceTitle.place(x=250, y=300)
    
    
    if(len(currentUser)!=0):#user is signed in specific elements displayed  
        if(currentUser[0][0] == 0):#user is a regular user
            stockTitle.config(text = "Quantity = "+str(searchBook(list.get(ACTIVE)[0],"isbn")[0][7]),font =("Arial", 12))
            stockTitle.place(x=250,y=350)
            buyBtn.place(x=250,y=400)
        else:#user is a admin
            stockTitle.config(text = "Quantity = ",font =("Arial", 12))
            stockTitle.place(x=250,y=350)
            stockBox.delete(0, 'end')
            stockBox.insert(END,searchBook(list.get(ACTIVE)[0],"isbn")[0][7])
            stockBox.place(x=330,y=353)
            editStockBtn.place(x=350,y=400)  
            deleteBtn.place(x=480,y=400)
            buyBtn.place(x=250,y=400)
    else:#user is NOT signed in specific elements displayed 
        stockTitle.config(text = "Quantity = "+str(searchBook(list.get(ACTIVE)[0],"isbn")[0][7]),font =("Arial", 12))
        stockTitle.place(x=250,y=350)
    print(list.get(ACTIVE))


list.bind('<Double-1>', select) #double click event declaration


def backButton():
    """
    backButton clears the current GUI then redirects the user to the default search/home screen

    """ 
    clearGUI()
    title.config(text = "Welcome to the Bookstore",font =("Arial", 14))
    list.place(x=250,y=100)
    drop.place(x=100,y=53)
    btn.place(x=560,y=50)
    box.place(x=250,y=55)
    browseLabel.place(x=10,y=50)
    title.pack()
    print(signedIn)
    global currentUser
    if(signedIn == True and currentUser[0][0] == 1):#admin specific gui displayed
        reg.place_forget()
        login.place_forget()
        logout.place(x=10,y=10)
        viewCartBtn.place(x=80,y=10)
        orderTrackBtn.place(x=10,y=80)
        editBankBtn.place(x=10,y=120)
        addBookBtn.place(x=10,y=160)
        statsBtn.place(x=10,y=200)
        
    elif(signedIn == True and currentUser[0][0] == 0):#regular user specific gui displayed
        reg.place_forget()
        login.place_forget()
        logout.place(x=10,y=10)
        viewCartBtn.place(x=80,y=10)
        orderTrackBtn.place(x=10,y=80)
        editBankBtn.place(x=10,y=120)
        
    else:#logged out user specific gui displayed
        reg.place(x=10,y=10)
        login.place(x=80,y=10)
        orderTrackBtn.place(x=10,y=80)
    

def trackButton():
    """
    trackButton loads the page to track orders

    """ 
    clearGUI()
    title.config(text = "Track Order",font =("Arial", 14))
    orderEntry.place(x=375,y=173)
    trackLabel.place(x=280,y=170)
    trackBtn.place(x=375,y=200)


def trackOrder():
    """
    trackOrder searches for an order from the value extracted by the user's input 
    in the text box entry, then finally displays whether it is a invalid order number or details
    about the order

    """ 
    if(orderEntry.get().isnumeric()):#check if entry is a number
        tracked = searchOrder(orderEntry.get())#search for order
        if(len(tracked) == 0):
            trackResultLabel.config(text = "Invalid Order Number",font =("Arial", 12))
            trackResultLabel.place(x=300,y=250)
        else:
            trackResultLabel.config(text = tracked[0][0]+"'s Order #"+orderEntry.get()+" is being shipped to "+tracked[0][2]+", "+tracked[0][1]+" in 10 days",font =("Arial", 12))
            trackResultLabel.place(x=150,y=250)
    

def statsButton():

    """
    statsButton loads the stats page onto the GUI

    """ 
    clearGUI()
    title.config(text = "Stats Page",font =("Arial", 14))
    statsBox.place(x=250,y=55)
    statsDrop.place(x=100,y=53)
    statsSearchBtn.place(x=560,y=50)

def searchStats():
    """
    searchStats grabs the value the user wants to lookup stats for from the entry box,
    the value that it represents from the drop down menu, and finally displays the 
    statistics of that entity in the bookstore

    """ 
    if(statsDrop.get().lower() == "author"):
        result = returnProfits(statsBox.get(), "author_name")#search for stats based on author name
        profitLabel.config(text = "Profit = $"+str(result[0]) ,font =("Arial", 14))
        numSoldLabel.config(text = "Copies Sold = "+str(result[1]) ,font =("Arial", 14))
        profitLabel.place(x=250,y=150)
        numSoldLabel.place(x=250,y=250)
    elif(statsDrop.get().lower() == "isbn"):
        result = returnProfits(statsBox.get(), "Book.isbn")#search for stats based on isbn
        print(result)
        profitLabel.config(text = "Profit = $"+str(result[0]) ,font =("Arial", 14))
        numSoldLabel.config(text = "Copies Sold = "+str(result[1]) ,font =("Arial", 14))
        profitLabel.place(x=250,y=150)
        numSoldLabel.place(x=250,y=250)
    else:
        result = returnProfits(statsBox.get(), statsDrop.get().lower())#search for stats based on any other entity
        print(result)
        profitLabel.config(text = "Profit = $"+str(result[0]) ,font =("Arial", 14))
        numSoldLabel.config(text = "Copies Sold = "+str(result[1]) ,font =("Arial", 14))
        profitLabel.place(x=250,y=150)
        numSoldLabel.place(x=250,y=250)

def loginButton():
    """
    loginButton loads the login page onto the GUI

    """ 
    clearGUI()
    title.config(text = "Login",font =("Arial", 14))
    usernameBox.place(x=285,y=55)
    usernameTitle.place(x=200,y=53)
    passwordBox.place(x=285,y=155)
    passwordTitle.place(x=200,y=153)
    signinBtn.place(x=250,y=200)

def registerButton():
    """
    registerButton loads the register page onto the GUI

    """ 
    clearGUI()
    title.config(text = "Register",font =("Arial", 14))
    emailBox.place(x=265,y=105)
    emailTitle.place(x=200,y=103)
    usernameBox.place(x=290,y=155)
    usernameTitle.place(x=200,y=153)
    passwordBox.place(x=285,y=205)
    passwordTitle.place(x=200,y=203)
    countryDrop.place(x=285, y=253)
    countryTitle.place(x=200,y=253)
    cityBox.place(x=285,y=303)
    cityTitle.place(x=200,y=303)
    addressBox.place(x=305, y=353)
    addressTitle.place(x=200,y=353)
    postalBox.place(x=305, y=403)
    postalTitle.place(x=200,y=403)
    signupBtn.place(x=250,y=445)
    signupAdminBtn.place(x=350,y=445)

def logoutButton():
    """
    logoutButton logs the current user out of the application

    """ 
    global currentUser, signedIn, cart
    
    #revert quantity changes
    for i in range(0,len(cart)):
        updateQuantity(cart[i][0][0],searchBook(cart[i][0][0],"isbn")[0][7]+1)
    
    #empty cart and log user out
    currentUser = []
    cart = []
    signedIn = False
    backButton()

def signin():
    """
    signin takes the user's username and password from the text box entrys to validate
    the user's information to finally log them in

    """ 

    user = searchCustomerByUserName(usernameBox.get())
    if(len(user) >0 and user[0][2] == passwordBox.get()):#log in user if the username and password both match
        print("logged in")
        global currentUser, signedIn
        currentUser = searchCustomerByUserName(usernameBox.get())
        signedIn = True
        backButton()
    else:#if data does not match, display failed to log in
        failedSignin.place(x=200,y=250)

def signup(num):
    """
    signup signs a user up and adds them into the system

    :param num: integer to determine whether user signed up as an admin or regular user

    """

    #sign customer up into the database and log them in
    addCustomer(num,usernameBox.get(),emailBox.get(),passwordBox.get(),addressBox.get(),countryDrop.get(),cityBox.get(),postalBox.get(),None,None,None,None,None,None,None)
    global currentUser, signedIn
    currentUser = searchCustomerByUserName(usernameBox.get())
    signedIn = True
    backButton()


def clearGUI():
    """
    clearGUI wipes the GUI completely, used for page rebuilding

    """ 
    bookTitle.pack_forget()
    bookTitle.place_forget()
    isbnTitle.place_forget()
    publisherTitle.place_forget()
    authorTitle.place_forget()
    genreTitle.place_forget()
    pageTitle.place_forget()
    priceTitle.place_forget()
    buyBtn.place_forget()
    emailBox.place_forget()
    usernameBox.place_forget()
    passwordBox.place_forget()
    emailTitle.place_forget()
    usernameTitle.place_forget()
    passwordTitle.place_forget()
    signinBtn.place_forget()
    signupBtn.place_forget()
    countryDrop.place_forget()
    countryTitle.place_forget()
    cityBox.place_forget()
    cityTitle.place_forget()
    postalBox.place_forget()
    postalTitle.place_forget()
    reg.place_forget()
    login.place_forget()
    logout.place_forget()
    btn.place_forget()
    browseLabel.place_forget()
    drop.place_forget()
    list.place_forget()
    addressTitle.place_forget()
    addressBox.place_forget()
    box.place_forget()
    viewCartBtn.place_forget()
    cartDisplay.place_forget()
    totalTitle.place_forget()
    checkoutBtn.place_forget()
    checkoutTitle.place_forget()
    cardNumBox.place_forget()
    cardNameBox.place_forget()
    cardExpDateBox1.place_forget()
    cardExpDateBox2.place_forget()
    cardCCVBox.place_forget()
    billstreetBox.place_forget()
    billcityBox.place_forget()
    billcountryDrop.place_forget()
    cardNumTitle.place_forget()
    cardNameTitle.place_forget()
    cardExpDateTitle.place_forget()
    cardCCVTitle.place_forget()
    billstreetTitle.place_forget()
    billcityTitle.place_forget()
    billcountryTitle.place_forget()
    confirmEditBankBtn.place_forget()
    editBankBtn.place_forget()
    checkoutTitle.place_forget()
    signupAdminBtn.place_forget()
    stockTitle.place_forget()
    stockBox.place_forget()
    editStockBtn.place_forget()
    deleteBtn.place_forget()
    addBookBtn.place_forget()
    confirmAddBtn.place_forget()
    titleBox.place_forget()
    isbnBox.place_forget()
    publisherBox.place_forget()
    authorBox.place_forget()
    genreBox.place_forget()
    pageBox.place_forget()
    priceBox.place_forget()
    statsBtn.place_forget()
    statsBox.place_forget()
    statsDrop.place_forget()
    statsSearchBtn.place_forget()
    profitLabel.place_forget()
    numSoldLabel.place_forget()
    trackBtn.place_forget()
    trackLabel.place_forget()
    trackResultLabel.place_forget()
    orderTrackBtn.place_forget()
    orderEntry.place_forget()
    restockDisplay.place_forget()
    failedSignin.place_forget()
    cartLabel.place_forget()
    
    
def buyButton():
    """
    buyButton adds a book to the cart of the current logged in user

    """ 

    if(searchBook(list.get(ACTIVE)[0],"isbn")[0][7]>0): #Order Book if the quantity is greater than 0
        cart.append(searchBook(list.get(ACTIVE)[0],"isbn"))
        updateQuantity(list.get(ACTIVE)[0],searchBook(list.get(ACTIVE)[0],"isbn")[0][7]-1)
        search()
        if(currentUser[0][0] == 0):#regular user specific display
            stockTitle.config(text = "Quantity = "+str(searchBook(list.get(ACTIVE)[0],"isbn")[0][7]),font =("Arial", 12))
            stockTitle.place(x=250,y=350)
        else:#admin specific display
            stockTitle.config(text = "Quantity = ",font =("Arial", 12))
            stockTitle.place(x=250,y=350)
            stockBox.delete(0, 'end')
            stockBox.insert(END,searchBook(list.get(ACTIVE)[0],"isbn")[0][7])
            stockBox.place(x=330,y=353)
        cartLabel.config(bg = "yellow", text = "Book Added to Cart",font =("Arial", 12))
        cartLabel.place(x=250,y=450)
    else:#Block user from checking out book if quantity is equal to 0
        cartLabel.config(bg = "red", text = "This Book is Out of Stock",font =("Arial", 12))
        cartLabel.place(x=250,y=450)
        print("Book is out of Stock")
    #print(cart)

def editStock():
    """
    editStock edits the quantity of the active book on screen

    """ 

    #update quantity of book and update display
    updateQuantity(searchBook(list.get(ACTIVE)[0],"isbn")[0][0],stockBox.get())
    search()
    stockBox.delete(0, 'end')
    stockBox.insert(END,searchBook(list.get(ACTIVE)[0],"isbn")[0][7])


def removeBook():
    """
    removeBook removes a book from the bookstore

    """ 
    #delete book and transport user back to home page after a second
    deleteBook(list.get(ACTIVE)[0])
    clearGUI()
    bookTitle.config(text = "THIS BOOK HAS BEEN DELETED" ,font =("Arial", 14))
    bookTitle.pack()
    search()
    bookTitle.after(1000,lambda: backButton())

def addButton():
    """
    addButton loads in the add book page for the admin

    """ 
    clearGUI()
    bookTitle.config(text = "Title = ",font =("Arial", 12))
    isbnTitle.config(text = "ISBN = ",font =("Arial", 12))
    publisherTitle.config(text = "Publisher = ",font =("Arial", 12))
    authorTitle.config(text = "Author = ",font =("Arial", 12))
    genreTitle.config(text = "Genre = ",font =("Arial", 12))
    pageTitle.config(text = "Number of Pages = ",font =("Arial", 12))
    priceTitle.config(text = "Price = $",font =("Arial", 12))  
    stockTitle.config(text = "Quantity = ",font =("Arial", 12))

    bookTitle.place(x=150,y=50)
    isbnTitle.place(x=150, y=100)
    publisherTitle.place(x=150, y=150)
    authorTitle.place(x=150, y=200)
    genreTitle.place(x=150, y=250)
    pageTitle.place(x=150, y=300)
    priceTitle.place(x=150, y=350)
    stockTitle.place(x=150,y=400)

    titleBox.place(x=300,y=53)
    isbnBox.place(x=300,y=103)
    publisherBox.place(x=300,y=153)
    authorBox.place(x=300,y=203)
    genreBox.place(x=300,y=253)
    pageBox.place(x=300,y=303)
    priceBox.place(x=300,y=353)
    stockBox.insert(END,"")
    stockBox.place(x=230,y=403)
    confirmAddBtn.place(x=400,y=450)




def addBookButton():
    """
    addBookButton adds a book to the database via admin input from text boxs

    """ 

    #add book and transport user back to home page after a second
    insertBook(isbnBox.get(),titleBox.get(),publisherBox.get(),authorBox.get(),genreBox.get(),pageBox.get(),priceBox.get(),stockBox.get())
    clearGUI()
    bookTitle.config(text = "THIS BOOK HAS BEEN ADDED" ,font =("Arial", 14))
    bookTitle.pack()
    search()
    bookTitle.after(1000,lambda: backButton())

def viewCart():
    """
    viewCart loads the checkout page, displaying the current cart of the user
     

    """ 
    clearGUI()
    cartDisplay.place(x=250,y=50)
    cartDisplay.delete(0,END)
    total = 0
    for i in range(0,len(cart)):
        total = total + cart[i][0][6]
        cartDisplay.insert(i,"Title: "+cart[i][0][1]+" Author: "+cart[i][0][3]+" Price: $"+str(cart[i][0][6]))

    totalTitle.config(text = "Total = $ "+str(total),font =("Arial", 12))
    totalTitle.place(x=250,y=400)
    global totalBackup
    totalBackup = total
    checkoutBtn.place(x=350,y=400)



def checkoutButton():
    """
    checkoutButton checks out all books in the cart of the current user and adds them 
    officially to the bookstore database

    """ 
    global currentUser, cart
    tempUser = checkIfCardisNull(currentUser[0][1])#check if the user has valid bank information
    orderCount = getOrderCount()#get next order id

    if(len(tempUser) == 0 and len(cart)!=0):#make a sale for every book in the cart if the cart is not empty and the user's bank info is legit
        
        tempStr = 'Restocked on Books: '
        for i in range(0,len(cart)):#iterate through every book and make a sale
            print(searchBook(cart[i][0][0],"isbn")[0][7])
            if(searchBook(cart[i][0][0],"isbn")[0][7]<=3):
                tempStr = tempStr + cart[i][0][1] +", "
                updateQuantity(cart[i][0][0],searchBook(cart[i][0][0],"isbn")[0][7]+10)
                
                
            makeSale(cart[i][0][0],cart[i][0][6])
        
        #add to the order database, empty the cart and update the GUI    
        addToOrder(orderCount[0][0], currentUser[0][1], totalBackup)
        cart = []
        restockDisplay.config(text = tempStr,font =("Arial", 12))
        restockDisplay.place(x=250,y=465)
        checkoutTitle.config(text = "Successfully Checked Out, Order Number: "+str(orderCount[0][0]),font =("Arial", 12))
        checkoutTitle.place(x=250,y=435)
    elif(len(tempUser) == 1):#display failure if the bank info is ilegitimate 
        checkoutTitle.config(text = "Bank Information is Invalid",font =("Arial", 12))
        checkoutTitle.place(x=250,y=435)
    #for i in range(0,len(cart)):
     #   total = total + cart[i][6]
      #  cartDisplay.insert(i,"Title: "+cart[i][1]+" Author: "+cart[i][3]+" Price: $"+str(cart[i][6]))

def editBankButton():
    """
    editBankButton loads the page to edit the users bank information

    """ 
    clearGUI()
    title.config(text = "Edit Bank Information",font =("Arial", 14))
    cardNumBox.place(x=290,y=105)
    cardNumTitle.place(x=180,y=103)
    cardNameBox.place(x=290,y=155)
    cardNameTitle.place(x=180,y=153)
    cardExpDateBox1.place(x=340,y=205)
    cardExpDateBox2.place(x=380,y=205)
    cardExpDateTitle.place(x=180,y=203)
    cardCCVBox.place(x=285, y=253)
    cardCCVTitle.place(x=180,y=253)
    billstreetBox.place(x=285,y=303)
    billstreetTitle.place(x=180,y=303)
    billcityBox.place(x=285, y=353)
    billcityTitle.place(x=180,y=353)
    billcountryDrop.place(x=300, y=403)
    billcountryTitle.place(x=180,y=403)
    confirmEditBankBtn.place(x=300,y=440)

def confirmEditBank():
    """
    confirmEditBank updates the user's bank information from the information
    entered in the text boxs

    """ 
    global currentUser
    dateStr = '20'+str(cardExpDateBox2.get())+"-"+str(cardExpDateBox1.get())+"-01" #form date to insert
    print(dateStr)

    #display success scenario if bank updates without issues
    if(updateCardInfo(cardNumBox.get(),cardNameBox.get(),dateStr,cardCCVBox.get(),billstreetBox.get(),billcityBox.get(),billcountryDrop.get(),currentUser[0][1])):
        checkoutTitle.config(text = "Successfully Edited Bank Account", font =("Arial", 12))
        currentUser = searchCustomerByUserName(currentUser[0][1])
        print(currentUser)
    else:#display failure if bank could not update
        checkoutTitle.config(text = "Invalid Bank Data, Re-Enter Bank Info", font =("Arial", 12))
    checkoutTitle.place(x=425,y=460)


def onClose():
    """
    onClose emptys the cart of the current user and reverts all quantity changes
    if the user decides to close the application

    """ 
    for i in range(0,len(cart)):
        updateQuantity(cart[i][0][0],searchBook(cart[i][0][0],"isbn")[0][7]+1)
    window.destroy()


window.protocol("WM_DELETE_WINDOW", onClose)

window.mainloop()
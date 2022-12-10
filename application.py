from tkinter import *
from tkinter import ttk
import sqlite3
from sqlite3 import Error

from sqlFunc import *
from datetime import datetime, date

folderName = ""

window = Tk()
window.title("Book Store")
window.geometry("750x500")


title = Label(window, text = "Welcome to the Bookstore")
title.config(font =("Arial", 14))
title.pack()

browseLabel = Label(window, text = "Browse by:")
browseLabel.config(font =("Arial", 12))
browseLabel.place(x=10,y=50)

currentUser = []
signedIn = False
cart = []
drop = ttk.Combobox(
    state="readonly",
    values=["Title", "Author", "ISBN", "Genre", "Publisher"]
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
buyBtn = Button(window, text = 'Add to Cart', bd = '3',command=lambda: buyButton())
buyBtn.config(height=2,width=10)

def search():
    searchList = searchBook(box.get(), drop.get().lower())
    list.delete(0,END)
    for i in range(0,len(searchList)):
        list.insert(i,searchList[i])
        #print(searchList[i])


def select(event):
    
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

    
    buyBtn.place(x=250,y=350)   

    print(list.get(ACTIVE))


list.bind('<Double-1>', select)

def backButton():
    clearGUI()
    list.place(x=250,y=100)
    drop.place(x=100,y=53)
    btn.place(x=560,y=50)
    box.place(x=250,y=55)
    browseLabel.place(x=10,y=50)
    title.pack()
    print(signedIn)
    if(signedIn == True):
        reg.place_forget()
        login.place_forget()
        logout.place(x=10,y=10)
        viewCartBtn.place(x=80,y=10)
        editBankBtn.place(x=10,y=80)
    else:
        reg.place(x=10,y=10)
        login.place(x=80,y=10)
    

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

signupBtn = Button(window, text = 'Sign Up', bd = '3',command=lambda: signup())
signupBtn.config(height=2,width=10)


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

def loginButton():
    clearGUI()
    usernameBox.place(x=285,y=55)
    usernameTitle.place(x=200,y=53)
    passwordBox.place(x=285,y=155)
    passwordTitle.place(x=200,y=153)
    signinBtn.place(x=250,y=200)

def registerButton():
    clearGUI()
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

def logoutButton():
    global currentUser, signedIn, cart
    
    for i in range(0,len(cart)):
        updateQuantity(cart[i][0][0],searchBook(cart[i][0][0],"isbn")[0][7]+1)
    currentUser = []
    cart = []
    signedIn = False
    backButton()

def signin():
    user = searchCustomerByUserName(usernameBox.get())
    if(user[0][2] == passwordBox.get()):
        print("logged in")
        global currentUser, signedIn
        currentUser = searchCustomerByUserName(usernameBox.get())
        signedIn = True
        backButton()

def signup():
    addCustomer(0,usernameBox.get(),emailBox.get(),passwordBox.get(),addressBox.get(),countryDrop.get(),cityBox.get(),postalBox.get(),None,None,None,None,None,None,None)
    global currentUser, signedIn
    currentUser = searchCustomerByUserName(usernameBox.get())
    signedIn = True
    backButton()
    
def clearGUI():
    bookTitle.pack_forget()
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
    
def buyButton():
    if(searchBook(list.get(ACTIVE)[0],"isbn")[0][7]>0):
        cart.append(searchBook(list.get(ACTIVE)[0],"isbn"))
        updateQuantity(list.get(ACTIVE)[0],searchBook(list.get(ACTIVE)[0],"isbn")[0][7]-1)
    else:
        print("Book is out of Stock")
    #print(cart)

cartDisplay = Listbox(window, width=50,height=20)

totalTitle = Label(window, text = "Total = $ ")

checkoutBtn = Button(window, text = 'Check Out', bd = '3',command=lambda: checkoutButton())
totalBackup = 0

checkoutTitle = Label(window, text = "Successfully Checked Out")
def viewCart():
    clearGUI()
    cartDisplay.place(x=250,y=50)
    cartDisplay.delete(0,END)
    total = 0
    for i in range(0,len(cart)):
        total = total + cart[i][6]
        cartDisplay.insert(i,"Title: "+cart[i][1]+" Author: "+cart[i][3]+" Price: $"+str(cart[i][6]))

    totalTitle.config(text = "Total = $ "+str(total),font =("Arial", 12))
    totalTitle.place(x=250,y=400)
    global totalBackup
    totalBackup = total
    checkoutBtn.place(x=350,y=400)

def checkoutButton():
    tempUser = checkIfCardisNull(currentUser[0][1])
    orderCount = getOrderCount()
    if(len(tempUser) == 0):
        global cart
        
        
            
        addToOrder(orderCount[0][0], currentUser[0][1], totalBackup)
        cart = []
        checkoutTitle.config(text = "Successfully Checked Out, Order Number: "+str(orderCount[0][0]),font =("Arial", 12))
        checkoutTitle.place(x=250,y=435)
    elif(len(tempUser) == 1):
        checkoutTitle.config(text = "Bank Information is Invalid",font =("Arial", 12))
        checkoutTitle.place(x=250,y=435)
    #for i in range(0,len(cart)):
     #   total = total + cart[i][6]
      #  cartDisplay.insert(i,"Title: "+cart[i][1]+" Author: "+cart[i][3]+" Price: $"+str(cart[i][6]))


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

def editBankButton():
    clearGUI()
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

checkoutTitle = Label(window, text = "Successfully Edited Bank Account")

def confirmEditBank():
    global currentUser
    dateStr = '20'+str(cardExpDateBox2.get())+"-"+str(cardExpDateBox1.get())+"-01"
    print(dateStr)
    if(updateCardInfo(cardNumBox.get(),cardNameBox.get(),dateStr,cardCCVBox.get(),billstreetBox.get(),billcityBox.get(),billcountryDrop.get(),currentUser[0][1])):
        checkoutTitle.config(text = "Successfully Edited Bank Account", font =("Arial", 12))
        currentUser = searchCustomerByUserName(currentUser[0][1])
        print(currentUser)
    else:
        checkoutTitle.config(text = "Invalid Bank Data, Re-Enter Bank Info", font =("Arial", 12))
    checkoutTitle.place(x=425,y=460)


def onClose():
    for i in range(0,len(cart)):
        updateQuantity(cart[i][0][0],searchBook(cart[i][0][0],"isbn")[0][7]+1)
    window.destroy()


window.protocol("WM_DELETE_WINDOW", onClose)

window.mainloop()
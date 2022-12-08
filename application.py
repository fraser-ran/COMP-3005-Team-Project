from tkinter import *
from tkinter import ttk
import sqlite3
from sqlite3 import Error

from sqlFunc import *


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
    bookTitle = Label(window, text = list.get(ACTIVE)[1])
    bookTitle.config(font =("Arial", 14))
    bookTitle.pack()

    isbnTitle = Label(window, text = "ISBN = "+str(list.get(ACTIVE)[0]))
    isbnTitle.config(font =("Arial", 12))
    isbnTitle.place(x=250, y=50)

    publisherTitle = Label(window, text = "Publisher = "+list.get(ACTIVE)[2])
    publisherTitle.config(font =("Arial", 12))
    publisherTitle.place(x=250, y=100)

    authorTitle = Label(window, text = "Author = "+list.get(ACTIVE)[3])
    authorTitle.config(font =("Arial", 12))
    authorTitle.place(x=250, y=150)

    genreTitle = Label(window, text = "Genre = "+list.get(ACTIVE)[4])
    genreTitle.config(font =("Arial", 12))
    genreTitle.place(x=250, y=200)

    pageTitle = Label(window, text = "Number of Pages = "+str(list.get(ACTIVE)[5]))
    pageTitle.config(font =("Arial", 12))
    pageTitle.place(x=250, y=250)

    priceTitle = Label(window, text = "Price = $"+str(list.get(ACTIVE)[6]))
    priceTitle.config(font =("Arial", 12))
    priceTitle.place(x=250, y=300)

    buyBtn = Button(window, text = 'Buy', bd = '3',command=lambda: search())
    buyBtn.config(height=2,width=10)
    buyBtn.place(x=250,y=350)   
    print(list.get(ACTIVE))


list.bind('<Double-1>', select)


btn = Button(window, text = 'Search', bd = '3',command=lambda: search())
btn.place(x=560,y=50)

reg = Button(window, text = 'Register', bd = '3')
reg.place(x=10,y=10)

login = Button(window, text = 'Login', bd = '3')
login.place(x=80,y=10)
window.columnconfigure(0,weight=1)


    
window.mainloop()
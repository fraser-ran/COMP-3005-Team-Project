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

btn = Button(window, text = 'Search', bd = '3',command=lambda: searchBook(box.get(), drop.get().lower()))
btn.place(x=560,y=50)

reg = Button(window, text = 'Register', bd = '3')
reg.place(x=10,y=10)

login = Button(window, text = 'Login', bd = '3')
login.place(x=80,y=10)
window.columnconfigure(0,weight=1)


    
window.mainloop()
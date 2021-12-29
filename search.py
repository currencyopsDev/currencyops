from tkinter import ttk
from tkinter import *
from tkinter import messagebox as msg
from functools import partial
class searchbox():
    def search(self,event):
        msg.showinfo("Info","Clicked to : "+event.widget.get())
    def clearout(self,event):
        event.widget.delete("0",END)
    def __init__(self,rootframe):
        area=Frame(rootframe)
        searchbox=ttk.Entry(area)
        searchbox.insert(0, 'Enter an asset to view...')
        searchbox.bind('<Return>', self.search)
        searchbox.bind('<FocusIn>', self.clearout)
        searchbox.place(anchor="center",relx=.3, rely=.5,width=300,relheight=0.06, relwidth=0.2)
        area.pack(fill=BOTH,side=LEFT,expand=True)
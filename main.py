import numpy as np
import pandas as pd
import yfinance as yf
from tkinter import ttk
from tkinter import *
import table as tb
import calendarbuilder as cb
import os,sys,queue,threading,platform
from rssfeed import rssfeed
from search import searchbox
from marketsummary import marketsummary
root=Tk()
if platform.system()=="Linux":
    root.attributes('-zoomed', True)
elif platform.system()=="Windows":
    root.state('zoomed')
root.title("Currencyops")
root.tk.call("source", sys.path[0]+"/azure.tcl")
root.tk.call("set_theme", "dark")
tabControl=ttk.Notebook(root)
homepage=ttk.Frame(tabControl)
exchange=ttk.Frame(tabControl)
crypto=ttk.Frame(tabControl)
stocks=ttk.Frame(tabControl)
calendar=ttk.Frame(tabControl)
tabControl.add(homepage,text="Home Page")
tabControl.add(exchange,text="Exchange Rates")
tabControl.add(crypto,text="Cryptocurrencies")
tabControl.add(stocks,text="Stocks")
tabControl.add(calendar,text="Economic Calendar")
Label(exchange,text="Loading...").place(relx=.5, rely=.5, anchor="center")
Label(crypto,text="Loading...").place(relx=.5, rely=.5, anchor="center")
Label(stocks,text="Loading...").place(relx=.5, rely=.5, anchor="center")
tables=[[exchange,sys.path[0]+"/watchlist/exchange"],[crypto,sys.path[0]+"/watchlist/cryptocurrencies"],[stocks,sys.path[0]+"/watchlist/stocks"]]
q=queue.Queue()
for table in tables:
    q.put(table)
def tableloader():
    while not q.empty():
        tableinfo=q.get()
        rootframe=tableinfo[0]
        watchlistpath=tableinfo[1]
        tb.tableBuilder(rootframe, watchlistpath)
        q.task_done()
theme="dark"
def change_theme():
    global theme
    if theme=="dark":
        root.tk.call("set_theme", "light")
        theme="light"
    else:
        root.tk.call("set_theme", "dark")
        theme="dark"
worker = threading.Thread(target=tableloader, daemon=True)
worker.start()
switch =ttk.Checkbutton(homepage, text='Switch Theme', style='Switch.TCheckbutton', command=change_theme)
switch.pack(side=TOP,anchor=NE)
scrollframe=cb.calendarBuilder(calendar)
separator =ttk.Separator(homepage, orient='horizontal').pack(fill=X)
marketsummary=marketsummary(homepage,["^IXIC","^DJI","AAPL","BTC-USD","GC=F","JPY=X","NFLX"])
separator =ttk.Separator(homepage, orient='horizontal').pack(fill=X)
searchbox=searchbox(homepage)
feeds=rssfeed(homepage)
tabControl.pack(expand=1,fill="both")
root.mainloop()
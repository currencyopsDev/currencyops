from tkinter import *
from tkinter import ttk
import numpy as np
import pandas as pd
import threading,random,time,threading,queue
from functools import partial # for looping buttons
import time
import yfinance as yf
import threading,queue
from tkinter import messagebox as msg
class tableBuilder():
    q=queue.Queue()
    status=""
    def print(self,parityname):
        msg.showwarning("Warning","Clicked to "+parityname)
    def buildTable(self,rootframe,parities):
        root=rootframe
        for widget in root.winfo_children(): # remove loading label
            widget.destroy()
        main_frame = Frame(root)
        main_frame.pack(fill=BOTH,expand=True)
        my_canvas=Canvas(main_frame)
        my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
        second_frame = Frame(my_canvas)
        my_canvas.create_window((0,0), window=second_frame, anchor="nw")
        tablehead=["Parity","Open","High","Low","Current Value","Updated On"]
        parities.insert(0,tablehead)
        for parityrow in range(0,len(parities)):
            paritydata=parities[parityrow]
            parityname=paritydata[0]
            for paritycolumn in range(0,len(paritydata)):
                Button(second_frame,text=paritydata[paritycolumn],highlightcolor=None,bd=0,relief="flat",anchor="w",takefocus=0,command=partial(self.print,parityname)).grid(row=parityrow,column=paritycolumn)
    def readConfig(self,filepath):
        parities=[]
        f=open(filepath,"r")
        for line in f.readlines():
            try:
                line=str(line).strip()
                data=yf.Ticker(line)
                lastinfo=data.history(period="1d",interval="1d")
                lastinfo=lastinfo.tail(1)
                lastprice=str(data.history(period="1d",interval="1m").tail(1)["Close"][0])[:8]
                lastinfo=[line,str(lastinfo["Open"][0])[:8],str(lastinfo["High"][0])[:8],str(lastinfo["Low"][0])[:8],lastprice,str(lastinfo.index.max())[:10]]
                parities.append(lastinfo)
            except Exception as err:
                print("Error while fetching "+str(line))
        return parities
    def __init__(self,mainframe,watchlistfile):
        parities=self.readConfig(watchlistfile)
        self.buildTable(mainframe, parities)
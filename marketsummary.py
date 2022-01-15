import numpy as np
import pandas as pd
import yfinance as yf
from tkinter import ttk
from tkinter import *
import io
class marketsummary:
    def createsummary(self,rootframe,indexes):
        root=rootframe
        main_frame=Frame(root)
        indexlabel=Label(main_frame,text="Market Overview : ",font=("Arial", 12)).pack(side=LEFT)
        for index in indexes:
            indexframe=Frame(main_frame)
            ticker=yf.Ticker(index)
            data=ticker.history(period="7d").tail(2)
            prevclose=data.iloc[0]["Close"]
            current=data.iloc[-1]["Close"]
            change=int(current)-int(prevclose)
            percentchange=str(100*(float(change)/float(prevclose)))[:5]
            indexlabel=Label(indexframe,text=index,font=("Arial", 12))
            currentlabel=Label(indexframe,text=str(round(current,2))+"$ ",font=("Arial", 12))
            if float(percentchange)>0:
                percentchangelabel=Label(indexframe,text=str(percentchange)+"% (+$"+str(change)+")",fg="green",font=("Arial", 11))
            elif float(percentchange)<0:
                percentchangelabel=Label(indexframe,text=str(percentchange)+"% (-$"+str(change)+")",fg="red",font=("Arial", 11))
            else:
                percentchangelabel=Label(indexframe,text=str(percentchange)+"% ($"+str(change)+")",font=("Arial", 11))
            delimiter=Label(indexframe,text=" | ")
            indexlabel.pack(side=LEFT)
            currentlabel.pack(side=LEFT)
            percentchangelabel.pack(side=LEFT)
            delimiter.pack(side=LEFT)
            indexframe.pack(side=LEFT)
        main_frame.pack(side=TOP,fill=X,pady=5)
    def __init__(self,rootframe,indexes):
        table=self.createsummary(rootframe,indexes)
from tkinter import ttk
from tkinter import *
from tkinter import messagebox as msg
from functools import partial
import numpy as np
import pandas as pd
import yfinance as yf
import plotly.graph_objs as go
class searchbox():
    def search(self,event):
        #msg.showinfo("Info","Clicked to : "+event.widget.get())
        self.ShowGraph(event.widget.get())
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
    def ShowGraph(self, ticker):
        choice = ticker
        choice = choice.upper()
        data = yf.download(tickers=choice, period='5y', interval='1d')
        fig = go.Figure()
        fig.add_trace(go.Candlestick(x=data.index, open=data['Open'], high=data['High'], low=data['Low'], close=data['Close'], name='market data'))
        fig.update_layout(title=choice + ' share price', yaxis_title='Stock Price')
        fig.update_xaxes(rangeslider_visible=True, rangeselector=dict(
            buttons=list([
                dict(count=24, label="1D", step="hour", stepmode="backward"),
                dict(count=120, label="5D", step="hour", stepmode="backward"),
                dict(count=720, label="1M", step="hour", stepmode="backward"),
                dict(count=2160, label="3M", step="hour", stepmode="backward"),
                dict(count=4320, label="6M", step="hour", stepmode="backward"),
                dict(count=8640, label="1Y", step="hour", stepmode="backward"),
                dict(count=43200, label="5Y", step="hour", stepmode="backward"),
                dict(step="all")])
            )
            )
        fig.show()
import numpy as np
import pandas as pd
import yfinance as yf
from tkinter import ttk
import tkinter as tk

root=tk.Tk()

tabControl=ttk.Notebook(root)

exchange=ttk.Frame(tabControl)
crypto=ttk.Frame(tabControl)
stocks=ttk.Frame(tabControl)

tabControl.add(exchange,text="Exchange Rates")
tabControl.add(crypto,text="Cryptocurrencies")
tabControl.add(stocks,text="Stocks")
tabControl.pack(expand=1,fill="both")


root.mainloop()
# # Python Project on Currency Converter

import requests,sys
from tkinter import *
import tkinter as tk
from tkinter import ttk
import re


class RealTimeCurrencyConverter():
    def __init__(self,url):
            self.data = requests.get(url).json()
            self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount): 
        initial_amount = amount 
        if from_currency != 'USD' : 
            amount = amount / self.currencies[from_currency] 
  
        # limiting the precision to 4 decimal places 
        amount = round(amount * self.currencies[to_currency], 4) 
        return amount

class App(tk.Tk):

    def __init__(self, converter):
        tk.Tk.__init__(self)
        self.call("source", sys.path[0]+"/azure.tcl")
        self.call("set_theme", "dark")
        self.winfo_toplevel().title('Currency Converter')
        self.currency_converter = converter
        style=ttk.Style()
        style.map('TCombobox', selectbackground=[('readonly', NONE)])
        #self.configure(background = 'blue')
        self.geometry("500x200")

        self.date_label = Label(self, text = f"1 Turkish Lira equals = {self.currency_converter.convert('TRY','USD',1)} USD \n Date : {self.currency_converter.data['date']}")
        self.date_label.place(x = 160, y= 20)

        # Entry box
        valid = (self.register(self.restrictNumberOnly), '%d', '%P')
        self.amount_field = ttk.Entry(self, justify = tk.CENTER,validate='key', validatecommand=valid,width=12)
        self.converted_amount_field_entry = ttk.Entry(self, justify = tk.CENTER,validate='key', validatecommand=valid,width=12)

        # dropdown
        self.from_currency_variable = StringVar(self)
        self.from_currency_variable.set("TRY") # default value
        self.to_currency_variable = StringVar(self)
        self.to_currency_variable.set("USD") # default value
        self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_currency_variable,values=list(self.currency_converter.currencies.keys()), state = 'readonly', width = 12, justify = tk.CENTER)
        self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_variable,values=list(self.currency_converter.currencies.keys()), state = 'readonly', width = 12, justify = tk.CENTER)

        # placing
        self.from_currency_dropdown.place(x = 30, y= 100)
        self.amount_field.place(x = 30, y = 150)
        self.to_currency_dropdown.place(x = 350, y= 100)
        #self.converted_amount_field.place(x = 346, y = 150)
        self.converted_amount_field_entry.place(x = 350, y = 150)
        
        # Convert button
        self.convert_button = ttk.Button(self, text = "Convert", command = self.perform) 
        self.convert_button.place(x = 200, y = 150)

    def perform(self):
        amount = float(self.amount_field.get())
        from_curr = self.from_currency_variable.get()
        to_curr = self.to_currency_variable.get()

        converted_amount = self.currency_converter.convert(from_curr,to_curr,amount)
        converted_amount = round(converted_amount, 2)
        self.converted_amount_field_entry.delete("0",END)
        self.converted_amount_field_entry.insert(0,str(converted_amount))
    
    def restrictNumberOnly(self, action, string):
        regex = re.compile(r"[0-9,]*?(\.)?[0-9,]*$")
        result = regex.match(string)
        return (string == "" or (string.count('.') <= 1 and result is not None))

def openConverter():
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = RealTimeCurrencyConverter(url)
    App(converter)
    mainloop()


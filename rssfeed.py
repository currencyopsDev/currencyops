import feedparser
import webbrowser
from functools import partial
from tkinter import *
from tkinter import ttk
class rssfeed():
    def getfeeds(self,url):
        feeds=[]
        d = feedparser.parse(url)
        for feed in d.entries:
            feeds.append([feed.title,feed.link])
        return feeds
    def openNews(self,feed):
        webbrowser.open(feed[1])
    def maketable(self,rootframe,feeds):
        root=rootframe
        main_frame = Frame(root,bd=1,relief="ridge")
        main_frame.pack(fill=BOTH,side=RIGHT,)
        Label(main_frame,text="NEWS",justify="center").pack(fill=X,side=TOP,anchor=NW)
        my_canvas=Canvas(main_frame)
        my_canvas.pack(side=LEFT,fill=BOTH)
        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y,anchor="w")
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
        second_frame = Frame(my_canvas)
        my_canvas.create_window((0,0), window=second_frame, anchor="w")
        for i in range(0,len(feeds)):
            feed=feeds[i]
            feedtitle=feed[0]
            feedlink=feed[1]
            Button(second_frame,text=feedtitle,relief="flat",wraplength=350,command=partial(self.openNews,feed)).grid(row=i,column=0)
    def __init__(self,rootframe):
        feeds=self.getfeeds("http://feeds.marketwatch.com/marketwatch/marketpulse/")
        self.maketable(rootframe, feeds)

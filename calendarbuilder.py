from tkinter import *
from tkinter import ttk
from economiccalendar import economiccalendar
class calendarBuilder():
    calendarlist=economiccalendar.getcalendar()
    def buildCalendar(self,rootframe):
        root=rootframe
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
        tablehead=["Date","Hour (UTC)","Country","Content","Previous","Consensus","Forecast"]
        self.calendarlist.insert(0, tablehead)
        for row in range(0,len(self.calendarlist)):
            line=self.calendarlist[row]
            requiredlines=[]
            try:
                if row==0:
                    for column in range(0,len(line)):
                        Button(second_frame,text=str(line[column]),highlightcolor=None,bd=0,relief="flat",anchor="w",takefocus=0).grid(row=row,column=column)
                elif row!=0:
                    requiredlines=[line[0],line[1],line[2],line[5],line[7],line[8],line[9]]
            except Exception as err:
                pass
            for column in range(0,len(requiredlines)):
                Button(second_frame,text=str(requiredlines[column]),highlightcolor=None,bd=0,relief="flat",anchor="w",takefocus=0).grid(row=row,column=column)
    def __init__(self,rootframe):
        self.buildCalendar(rootframe)

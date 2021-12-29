import requests
from bs4 import BeautifulSoup
class economiccalendar():
    def datelocator(htmlcontent,tableheads,indexnumber): #finding the row's date by comparing row's index and tableheads indexes
        proximity={}
        for head in tableheads:
            index=htmlcontent.find(head)
            proximity[index]=head
        indexlist=list(proximity)
        indexlist.reverse()
        for x in indexlist:
            if indexnumber>int(x):
                return proximity.get(x)
    @classmethod
    def getcalendar(self) -> list:
        r=requests.get("https://tradingeconomics.com/calendar")
        soup=BeautifulSoup(r.content,'html.parser')
        table=soup.find("table",attrs={"id":"calendar"})
        tableinner=str(table)
        tableheads=soup.find_all("thead",attrs={"class":"table-header"})
        heads=[]
        output=[]
        for head in tableheads: # gets the date from the tableheads
            tablehead=head.find("th",attrs={"colspan":"3"})
            date=str(tablehead.text).strip()
            heads.append(date)
        tablerows=table.find_all("tr")
        for tablerow in tablerows:  
            rowindex=tableinner.find(str(tablerow))
            rowdate=self.datelocator(tableinner,heads,int(rowindex))
            row=[]
            rowitems=tablerow.find_all("td")
            for rowitem in rowitems:
                temp=str(rowitem.text).strip().replace(" "*24, " ")
                if len(temp)>0:
                    row.append(temp.replace("\r", "").replace("\n", ""))
                elif len(temp)==0:
                    row.append(" ")
            if len(row)>2:  #eliminating junk entries
                row.insert(0,rowdate)
                output.append(row)
        return output
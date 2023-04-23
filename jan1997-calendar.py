#import library
import csv
from urllib .request import Request, urlopen as uReq
from bs4 import BeautifulSoup as soup

#web url
myUrl = 'https://www.timeanddate.com/calendar/?year=1997&country=69'

#request
uClient = uReq(myUrl)
page_html = uClient.read()
uClient.close()

#parse page
page_soup = soup(page_html,"html.parser")

#create csv
filename = "january1997.csv"
f = open(filename, "w", newline='')
writer = csv.writer(f)
headers = ["Day"]
writer.writerow(headers)

#find calendar table on page
calendar_table = page_soup.find("table", {"class": "ca ca1"})

if calendar_table is not None:
    print("found")
else:
    print("table not found")

#extract data from calendar
calendar_data = []
for row in calendar_table.find_all("tbody"):
    calendar_row = []
    for cell in row.find("tr",{"class": "c1"}):
        day = cell.find("td")
        if day:
            writer.writerow([day.text.strip()])

f.close()
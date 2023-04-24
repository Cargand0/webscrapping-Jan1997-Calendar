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
with open(filename, "w", newline='') as f:
    writer = csv.writer(f)
    headers = ["Day"]
    writer.writerow(headers)

#find calendar table on page
calendar_table = page_soup.find("td", {"class": "cbm cba tc cmi"})

if calendar_table is not None:
    print("found")
else:
    print("table not found")

#extract data from calendar
calendar_data = []
for row in calendar_table.find_all("table", {"class": "ca ca1"}):
    calendar_row = []
    for cell in row.find("tr"):
        day = cell.find("tr", {"class": "c1"})
        if day:
            writer.writerow([day.text.strip()])

f.close()
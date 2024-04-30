import csv #used to read/write csv files
import requests #access websites
from bs4 import BeautifulSoup #webscraping toolsets

url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s' #URL

response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}) #GET request

html = response.content #pull the content from GET request

soup = BeautifulSoup(html) 
table = soup.find('tbody', attrs={'class': 'stripe'})

list_of_rows=[]
#sorts through the table of information
for row in table.findAll('tr'):
    list_of_cells = [] #establish list to hold information to export
    for cell in row.findAll('td')[:-1]: #sorts through information from each cell
        text = cell.text #hold cell.text value into text variable
        list_of_cells.append(text) #append text into list created earlier
    list_of_rows.append(list_of_cells) #append list into another list, like a spreadsheet

outfile = open("inmates.csv", "w") #tell program to open a csv file, and w = write
writer = csv.writer(outfile) #write into a new file
writer.writerow(["Last", "First", "Middle", "Suffix", "Gender", "Race", "Age", "City", "State"])
writer.writerows(list_of_rows) #import the list_of_rows into the csv file
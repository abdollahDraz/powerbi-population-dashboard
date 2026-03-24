from bs4 import BeautifulSoup
import requests
import pandas as pd
URL = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'

headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(URL, headers=headers)
# print(response
soup = BeautifulSoup(response.text ,"html.parser" ) # change the page to object you can analysis it .

data = []

table = soup.find("table", class_="wikitable")

rows = table.findAll("tr")

for row in rows:
    cols = row.findAll("td")

    if len(cols) >= 4 :
        Country = cols[0].text.strip()
        if Country == 'World':
            continue
        Populotion = cols[1].text.strip().replace(',','')
        Persentage = cols[2].text.strip().replace('%','')
        Date = cols[3].text.strip()
        data.append([Country, Populotion, Persentage, Date])

Data_Frame = pd.DataFrame(data ,columns = ['Country Code', 'Populotion', 'Persentage', 'Date'])
print(Data_Frame.head())
Data_CSV = Data_Frame.to_csv('Data.csv')

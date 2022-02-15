import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib3


url = 'https://gh.soccerway.com/players/players_abroad/ghana/'

#added header to bypass error of no permission to site on the server
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
}

webpage = requests.get(url=url,headers=header)
#print(webpage.status_code)

soup = BeautifulSoup(webpage.text, 'lxml')
#print(soup)

table = soup.find('table',class_='playersabroad table')

col = ['player','league','team','country']
players_data = pd.DataFrame(columns=col)
country = ''
cleaned = ''

for j in table.find_all('tr')[1:]:
    row = [i.text for i in j]

    if len(row) == 3:
        country = row[1]
    else:
        row.append(country)
        clean_row = [] 
        for data in row:
            if data != '\n':
                cleaned = data.strip()
                clean_row.append(cleaned) 
        length = len(players_data)
        players_data.loc[length] = clean_row  
    
#extract to csv
players_data.to_csv(r'C:\Users\user\Documents\players_scrapper\players.csv',index=False)

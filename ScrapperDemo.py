import requests
from bs4 import BeautifulSoup

#get url
page = requests.get ('https://www.imdb.com/chart/top/')
soup = BeautifulSoup(page.content,'html.parser')

links = soup.select(" table > tbody > tr > td.titleColumn > a") # Selecting all of the anchors with titles
first10 = links[:10] # Keep only the first 10 anchors
for anchor in first10:
    print(anchor.text) # Display the innerText of each anchor
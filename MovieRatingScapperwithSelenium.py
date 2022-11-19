import requests
import csv
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


option = webdriver.ChromeOptions()
option.add_argument('--headless')
driver =webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)
driver.get('https://www.imdb.com/chart/top/')
soup = BeautifulSoup(driver.page_source,'html.parser')
totalScrappedInfo = []
for i in range(1, 10):
    xpathtitle = "//table[@class='chart full-width']//child::tr["+str(i)+"]//child::td[@class='titleColumn']"
    titlename = driver.find_element(By.XPATH,xpathtitle)
    titlerating = titlename.find_element(By.XPATH,"//following-sibling::td[@class='ratingColumn imdbRating']")
    ScrapperInfo = {
        "title": titlename.text,
        "Rating":  titlerating.text
        }
    totalScrappedInfo.append(ScrapperInfo)
print(totalScrappedInfo)

#Write the output in JSON file
file = open('moviesRating.json', mode='w')
file.write(json.dumps(totalScrappedInfo))

#Write the output in CSV file 
writer = csv.writer(open("movies.csv", 'w', newline=''))
for movie in totalScrappedInfo:
    writer.writerow(movie.values())






# titlename = driver.find_element(By.XPATH,"//table[@class='chart full-width']//child::tr//child::td[@class='titleColumn']//a")
# first10title = titlename[0:10]
# IMDBratingx = titlename.find_element
# IMDBrating = driver.find_elements(By.XPATH, "//table[@class='chart full-width']//child::tr//child::td[@class='ratingColumn imdbRating']")
# first10rating= IMDBrating[0:10]
# for title in first10title:
#     ScrapperInfo = {
#         "title": title.text,
#         "Rating":  first10rating[title].text


#     }
    



# links = soup.select(" table > tbody > tr > td.titleColumn > a") # Selecting all of the anchors with titles
# first10 = links[:10] # Keep only the first 10 anchors
# for anchor in first10:
#     print(anchor.text) # Display the innerText of each anchor

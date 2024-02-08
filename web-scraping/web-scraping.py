# download webdriver for chrome and set the PATH variable to that folder
PATH = "~/Downloads/chromedriver"


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re
import pandas as pd

# create a class to hold scraped results information
class libraryEntity():
    ID = 0
    Author = "unknown"
    Title = "unknown"

    def __init__(self, ID, Author, Title):
        self.ID = ID
        self.Author = Author
        self.Title = Title

    def showDetails(self):
        print("Result " + str(self.ID) + " authored by " + self.Author + " title is: " + self.Title)

# Extracts text from scraped content.
def extractText(data):
    text = data.get_attribute('innerHTML')
    soup = BeautifulSoup(text, features="lxml")
    content = soup.get_text()
    return content

# set the address of the website to scrape
URL = "https://libgen.is/"
browser = webdriver.Chrome()
browser.get(URL)

# Give the browser time to load all content.
time.sleep(3)

# Find the search input.
search = browser.find_element(By.CSS_SELECTOR,"#searchform")
search.send_keys("math")

# Find the search button - this is only enabled when a search query is entered
button = browser.find_element(By.CSS_SELECTOR,"#searchform+input")
button.click()  # Click the button.

# scrape the first three pages
IDs = browser.find_elements(By.CSS_SELECTOR,".c td:nth-child(1)")
authors = browser.find_elements(By.CSS_SELECTOR,".c td:nth-child(2)")
titles = browser.find_elements(By.CSS_SELECTOR,".c td:nth-child(3)")
print(titles
      )

resultList = []
for i in range(0, len(titles)):
    # extract title and add to list.
    title = extractText(titles[i])

    # extract description and add to list.
    ID = extractText(IDs[i])

    author = extractText(authors[i])
    library_entity = libraryEntity(ID, author, title)
    resultList.append(library_entity)
# # Find the search button - this is only enabled when a search query is entered
button = browser.find_element(By.CSS_SELECTOR,"#paginator_example_top td:nth-child(2)")
button.click()  # Click the button.

IDs2 = (browser.find_elements(By.CSS_SELECTOR,".c td:nth-child(1)"))
authors2 = (browser.find_elements(By.CSS_SELECTOR,".c td:nth-child(2)"))
titles2 = (browser.find_elements(By.CSS_SELECTOR,".c td:nth-child(3)"))
for i in range(0, len(titles2)):
    # extract title and add to list.
    title = extractText(titles2[i])

    # extract description and add to list.
    ID = extractText(IDs2[i])

    author = extractText(authors2[i])
    library_entity = libraryEntity(ID, author, title)
    resultList.append(library_entity)
# Find the search button - this is only enabled when a search query is entered
button = browser.find_element(By.CSS_SELECTOR,"#paginator_example_top td:nth-child(3)")
button.click()  # Click the button.

IDs3 = (browser.find_elements(By.CSS_SELECTOR,".c td:nth-child(1)"))
authors3 = (browser.find_elements(By.CSS_SELECTOR,".c td:nth-child(2)"))
titles3 = (browser.find_elements(By.CSS_SELECTOR,".c td:nth-child(3)"))
#
for i in range(0, len(titles3)):
    # extract title and add to list.
    title = extractText(titles3[i])

    # extract description and add to list.
    ID = extractText(IDs3[i])

    author = extractText(authors3[i])
    library_entity = libraryEntity(ID, author, title)
    resultList.append(library_entity)


# Show the content.
for i in range(1, len(resultList)):
    print("\n********************")
    resultList[i].showDetails()

# store the extracted data into a pandas dataframe
result_df = pd.DataFrame(columns=['ID', 'Title', 'Author'])

for i in range(1, len(resultList)):
    result_df.loc[i - 1] = [resultList[i].ID, resultList[i].Title, resultList[i].Author]

print(result_df)
# save the dataframe to a csv file
result_df.to_csv("./books_df.csv")
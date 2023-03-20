from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from functions import pgScrape

options = Options()
options.headless = False
# options.add_argument('window-size=1920x1080')

site = 'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273'
#path = 'chromedriver'
driver = webdriver.Chrome(options=options)
driver.get(site)

currentPg = 1
lastPg = 20

linkArray = []

while currentPg <= lastPg:
    print(f"Current Page: {currentPg}")
    listing = driver.find_elements('xpath','//div[contains(@class,"search-item")]')
    links = driver.find_elements('xpath', '//a[contains(@class,"title")]')
    #NEED TO CREATE LIST OF LINKS ON THE PAGE - GET THE ATTRIBUTE VALUE
    for link in links:
        href = link.get_attribute("href")
        #print(href)
        linkArray.append(href)
    # pagination
    page = driver.find_element('xpath', '//div[@class="pagination"]')
    try:
        nextPg = page.find_element(By.PARTIAL_LINK_TEXT, 'Next')
        nextPg.click()
    except:
        print("#####################################")
        print("##### No more pages to scrape! ######")
        print("#####################################")
        pass
    currentPg = currentPg + 1

print(linkArray)
#set counter to break amount of pages navigated - set to 10 for now

#THEN OPEN EACH LISTING AND PULL THE DATA FROM THOSE PAGES

#for list in listing:
    #print(list.text)
driver.quit()


for links in linkArray:
    pgScrape(links)


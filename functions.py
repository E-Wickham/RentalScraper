def pgScrape(link):
    from selenium import webdriver 
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    import time
    import re
    from listingClass import Listing
    import pgeocode
    
    DOWNLOAD_URL = [
        "CA_full.csv.zip",
        "https://download.geonames.org/export/zip/CA_full.csv.zip",
        "https://symerio.github.io/postal-codes-data/data/geonames/CA.txt",
    ]

    options = Options()
    options.headless = True
    # options.add_argument('window-size=1920x1080')

    page = webdriver.Chrome(options=options)
    page.get(link)
    time.sleep(1)
    try:
        title = page.find_element('xpath', '//h1[contains(@class,"title")]').get_attribute("innerHTML")
        print('title \n')
        print(title)
        print('#############')
        unitRow = page.find_element('xpath', '//div[contains(@class,"unitRow")]')
        bedsS = unitRow.find_element('xpath', '//li[contains(@class,"noLabelAttribute")][2]/span').get_attribute("innerHTML")
        beds = re.sub('\D', '', bedsS)
        if beds == "":
            beds = 0
        info = page.find_element('xpath', '//div[contains(@class,"realEstateTitle")]')
        priceS = info.find_element('xpath', '//div[contains(@class,"priceWrapper")]')
        price = re.sub('\D', '', priceS.text)
        if price == "":
            price = 0
        location = page.find_element('xpath','//div[contains(@class,"locationContainer")]')
        address = location.find_element('xpath', '//span[contains(@class,"address")]').get_attribute("innerHTML")
        try:
            postalcode = (re.findall(r'[A-Z]{1}[0-9]{1}[A-Z]{1}\s*[0-9]{1}[A-Z]{1}[0-9]{1}', address))[0]
        except:
            postalcode = 'n/a'
        
        print(link)
        print(address)
        print(postalcode)
        print(price)
        print(beds)

        ### CREATE COORDINATES

        nomi = pgeocode.Nominatim('ca')

        try:
            coordinate = nomi.query_postal_code(postalcode[0:3])
            lat = str(coordinate["longitude"])
            long = str(coordinate["latitude"])
            print('coordinate function works')
        except:
            lat = '0'
            long = '0'
            print('coordinate function did not work')
        insert = Listing(title, address, postalcode, beds, price, link, lat, long)
        insert.dbInsert()
    except:
        print(f'failure scraping link: {link}')
        pass

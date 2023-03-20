# RentalScraper
A webscraper to scrape links from kijiji using selenium and enter them into a mysql database

# How does it work? 
1. The scraper opens a Chrome browser in selenium and travels to the paginated list of units. It travels through the first 20 pages on the site and collects links, places them into a list. 
2. A second function (pgScrape) cycles through every url on the list and collects specific data from the individual listings
3. Based on the data provided (first three digits of postal code) geolocation data is generated for the interactive map included with scraper story. 
4. All data is placed into an object (to ensure uniformity of data) and uploaded into a mysql database.

# Explanation of files 

## ChromeDriver.exe
This is the file that allows the script to open a browser. The ChromeDriver must be the same release as the chrome browser currently installed on your computer

## functions.py 
This file includes the function that pulls all the data from a single kijiji page. It opens the browser, finds the data and saves it into variables. It also generates specific geolocation data based on the postal codes

## kijiji.py 
This file collects the links and places them in a list to iteratively run the pgScrape function located in functions.py on. 

## listingClass.py
This file creates an object and includes specific methods in it that allow for uploading data into a database. This is the final step of all the data that is collected. In the other files, the links to scrape are first collected and then gone through one by one. Then the data is pulled and cleaned up to make uploading as clean a process as possible. To ensure no errors happen in the upload, the data from each individual scrape is first put into an object, and then is uploaded through its own method. If the data is not prepared/cleaned well enough, it will not upload into the database. 

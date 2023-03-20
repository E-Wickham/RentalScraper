# RentalScraper
A webscraper to scrape links from kijiji using selenium and enter them into a mysql database

# How does it work? 
1. The scraper opens a Chrome browser in selenium and travels to the paginated list of units. It travels through the first 20 pages on the site and collects links, places them into a list. 
2. A second function (pgScrape) cycles through every url on the list and collects specific data from the individual listings
3. Based on the data provided (first three digits of postal code) geolocation data is generated for the interactive map included with scraper story. 
4. All data is placed into an object (to ensure uniformity of data) and uploaded into a mysql database.

from datetime import date 
import mysql.connector
import re

class Listing():
    def __init__(self, title, address, postalcode, beds, price, url, lat, long):
        self.title = title
        self.address = address
        self.postalcode = postalcode
        self.beds = beds
        self.price = price 
        self.url = url
        self.day = date.today()
        self.lat = lat
        self.long = long

    def dbInsert(self):
        # DB information to connect to localhost REPLACE WITH LOCALHOST
        mydb = mysql.connector.connect(
        host="#####",
        port="#####",
        user="#####",
        password="#####",
        database ="#####"
        )
        #get everything from the listing table
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM listings")
        result = mycursor.fetchall()
        #check if the postal code and price matches any of the existing entries

        for elem in result:
            if self.postalcode in elem and self.price in elem:
                newListing = False
                break
            else: 
                newListing = True


        #TO DO - CHECK TO SEE IF 'WANTED: ' STRING IS IN TITLE TO ENSURE ANY LISTINGS SEEKING HOUSING ARENT PICKED UP

        #if newlisting does not exist in the table, add it to the table
        if newListing == True:
            print('listing does not exist in record. Creating new entry:')
            sqlColumnists = "INSERT INTO listings (title, address, city, postalcode, bedrooms, price, url, scrapedate, lat, lon) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            valColumnists = (self.title, self.address, 'Toronto', self.postalcode, self.beds, self.price, self.url, self.day, self.lat, self.long)
            mycursor.execute(sqlColumnists, valColumnists)
            print("Adding to database: ", self.address, "\n", self.url)
            mydb.commit()
        else:
            print(self.address,"exists in record: ")

#list1 = Listing('1234','l5l4s7', 2, 44444, 'www.google.ca', 54.3334, -64.2354)
#print(list1.day)
#list1.dbInsert()
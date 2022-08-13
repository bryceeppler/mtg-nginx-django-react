import requests
from bs4 import BeautifulSoup
import string


class HouseOfCardsSpider():
    def __init__(self, cardName, url):
        self.url = url
        self.cardName = cardName

    def compareCardNames(self, cardName, cardName2):
        """
        compares two card names and returns true if they are the same
        """
        # remove all punctuation from card names
        cardName = cardName.translate(str.maketrans('', '', string.punctuation)).lower()
        cardName2 = cardName2.translate(str.maketrans('', '', string.punctuation)).lower()
        if cardName in cardName2:
            return True
        else:
            return False
        
    
    def getStock(self):
        """
        returns a stock list for the card
        """
        page = requests.get(self.url)
        sp = BeautifulSoup(page.text, 'html.parser')
        cards = sp.select('div.productCard__card')

        inStockList = []

        for card in cards:

            # Product tiles are split into upper and lower divs
            productCardLower = card.select_one('div.productCard__lower')
            productCardUpper = card.select_one('div.productCard__upper')

            # check to see its a magic card
            if card['data-producttype'] != 'MTG Single':
                continue

            # check to see name is correct
            checkName = productCardLower.select_one('a').getText()
            if not self.compareCardNames(self.cardName, checkName):
                continue


            stockList = []
            conditions = productCardLower.select('li.productChip')
            for c in conditions:
                if c['data-variantavailable'] == 'true':
                    condition = c.getText().strip()
                    price = float(c['data-variantprice']) / 100
                    stockList.append((condition, price))

            # if stockList is empty, continue
            if not stockList:
                continue

            # <a> tag has href pointing to card's page and inner text is the card's name
            tag = productCardLower.select_one('a')
            name = tag.getText()
            baseUrl = 'https://houseofcards.ca'
            link =  baseUrl + tag.get('href')

            # image
            imageUrl = productCardUpper.select_one('img').attrs['data-src']
            imageUrl = imageUrl.replace('//', 'https://')

            # set name
            setName = productCardLower.select_one('p.productCard__setName').getText()


            inStockList.append({
                'name': name,
                'link': link,
                'image': imageUrl,
                'set': setName,
                'stock': stockList
            })

        return inStockList

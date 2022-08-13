import requests
from bs4 import BeautifulSoup
import string

class GauntletSpider():
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
        cards = sp.select('li.product')

        inStockList = []

        for card in cards:
            # each card has an inner shell div
            cardShell = card.select_one('div.inner')

            # check to see its a magic card
            if not card['data-catalog-id']:
                continue

            # check to see name is correct
            checkName = cardShell.select_one('div.image a')['title']
            if not self.compareCardNames(self.cardName, checkName):
                continue

            stockList = []

            conditions = cardShell.select('div.variant-row')
            for c in conditions:
                if 'no-stock' in c['class']:
                    continue
                condition = c.select_one('span.variant-description').getText()
                if "NM" in condition:
                    condition="NM"
                elif "Light" in condition:
                    condition="LP"
                elif "Moderate" in condition:
                    condition="MP"
                elif "Heavy" in condition:
                    condition="HP"
                
                price = float(c.select_one('form.add-to-cart-form')['data-price'].replace('CAD$ ', ''))
                # not sure why but some prices go in duplicate, do this to guard
                if (condition, price) not in stockList:
                    stockList.append((condition, price))

            # if stockList is empty, continue
            if not stockList:
                continue

            name = cardShell.select_one('div.image a')['title']
            baseUrl = 'https://www.gauntletgamesvictoria.ca'
            link = baseUrl + cardShell.select_one('div.image a')['href']

            #image
            imageUrl = cardShell.select_one('img')['src']
        
            # set name
            setName = cardShell.select_one('span.category').getText()

            inStockList.append({
                'name': name,
                'link': link,
                'image': imageUrl,
                'set': setName,
                'stock': stockList
                }
            )
        return inStockList


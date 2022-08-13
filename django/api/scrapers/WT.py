import requests
from bs4 import BeautifulSoup
import string

class WTSpider():
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

        cards = sp.select('table.invisible-table tr')

        inStockList = []

        for card in cards:
            checkNameTag = card.select('td')[1]
            checkName = checkNameTag.select_one('a')
            if not checkName:
                continue
            if not self.compareCardNames(self.cardName, checkName.getText()):
                continue
            # check to see its a magic card and in stock
            stockList = []
            conditions = card.select('tr.variantRow')
            for c in conditions:
                condition = c.select_one('td.variantInfo').getText().replace('Condition: ', '').replace('-Mint, English', '')
                if "Brand New" in condition: # then it's not a MTG single
                    continue
                elif "NM" in condition:
                    condition="NM"
                elif "Slightly" in condition:
                    condition="LP"
                elif "Moderately" in condition:
                    condition="MP"
                elif "Heav" in condition:
                    condition="HP"
                price = float(c.select('td')[1].getText().replace('CAD$ ', ''))
                if (condition, price) not in stockList:
                    stockList.append((condition, price))
                
            # if stockList is empty, continue
            if not stockList:
                continue

            nameTag = card.select('td')[1]
            name = nameTag.select_one('a').getText()

            baseUrl = 'https://www.kanatacg.com'
            link = baseUrl + nameTag.select_one('a')['href']

            imageUrl = card.select_one('td a')['href']

            setNameTag = card.select('td')[1]
            setName = setNameTag.select_one('small').getText()
            inStockList.append({
                'name': name,
                'link': link,
                'image': imageUrl,
                'set': setName,
                'stock': stockList
                }
            )
        return inStockList
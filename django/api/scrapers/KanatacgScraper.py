from bs4 import BeautifulSoup
import requests
import string

class KanatacgScraper():
    def __init__(self, cardName):
        self.cardName = cardName
        self.results = {}
        self.baseUrl = 'https://www.kanatacg.com'
        self.searchUrl = self.baseUrl + '/products/search?query='
        self.url = self.createUrl()

    def getResults(self):
        return self.results

    def createUrl(self):
        url = self.searchUrl
        nameArr = self.cardName.split()
        for word in nameArr:
            url +=word
            if word != nameArr[len(nameArr)-1]: # then we don't have last item, add +
                url+= '+'
            else: pass
        return url


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


    def scrape(self):
        print('Scraping ' + self.url)
        page = requests.get(self.url)

        print('Retreiving card list')
        sp = BeautifulSoup(page.text, 'html.parser')
        cards = sp.select('table.invisible-table tr')

        stockList = []

        for card in cards:
            # Check to see it is a magic card
            # TODO

            # Verify card name is correct
            checkNameTag = card.select('td')[1]
            checkName = checkNameTag.select_one('a')        
            if not checkName:
                continue
            if not self.compareCardNames(self.cardName, checkName.getText()):
                continue

            # For this card variant, get the stock
            variantStockList = []
            variantConditions = card.select('tr.variantRow')

            # For each item get the condition and price
            for c in variantConditions:
                condition = c.select_one('td.variantInfo').getText().replace('Condition: ', '').replace('-Mint, English', '')
                if "Brand New" in condition: # then it's not a MTG single
                    continue
                elif "NM" in condition:
                    condition="NM"
                elif "Slight" in condition:
                    condition="LP"
                elif "Moderate" in condition:
                    condition="MP"
                elif "Heav" in condition:
                    condition="HP"
                price = float(c.select('td')[1].getText().replace('CAD$ ', ''))
                if (condition, price) not in variantStockList:
                    variantStockList.append((condition, price))
                
            # If stockList is empty, continue
            if not variantStockList:
                continue

            name = card.select('td')[1].select_one('a').getText()
            link = self.baseUrl + card.select('td')[1].select_one('a')['href']
            imageUrl = card.select_one('td a')['href']
            setName = card.select('td')[1].select_one('small').getText()

            results = {
                'name': name,
                'link': link,
                'image': imageUrl,
                'set': setName,
                'stock': variantStockList
            }
            stockList.append(results)

        self.results = stockList
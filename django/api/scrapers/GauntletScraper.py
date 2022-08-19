from bs4 import BeautifulSoup
import requests
import string

class GauntletScraper():
    def __init__(self, cardName):
        self.cardName = cardName
        self.results = []
        self.baseUrl = 'https://www.gauntletgamesvictoria.ca'
        self.searchUrl = self.baseUrl + '/products/search?q='
        self.url = self.createUrl()

    def getResults(self):
        return self.results

    def createUrl(self):
        url = self.searchUrl
        nameArr = self.cardName.split()
        for word in nameArr:
            url += word
            if word != nameArr[len(nameArr)-1]: # then we don't have last item, add +
                url+= '+' 
            else: url+= '&c1'
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
        cards = sp.select('li.product div.inner')

        stockList = []

        for card in cards:
            # Check to see it is a magic card
            # TODO

            # Verify card name is correct
            checkName = card.select_one('div.image a')['title']
            if not self.compareCardNames(self.cardName, checkName):
                continue

            # For this card variant, get the stock
            variantStockList = []
            variantConditions = card.select('div.variant-row')

            # For each item, get the condition and price
            for c in variantConditions:
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

                # Verify condition and price are not duplicates
                if (condition, price) not in variantStockList:
                    variantStockList.append((condition, price))

            if len(variantStockList) == 0:
                continue

            name = card.select_one('div.image a')['title']
            link = self.baseUrl + card.select_one('div.image a')['href']
            imageUrl = card.select_one('img')['src']
            setName = card.select_one('span.category').getText()

            results = {
                'name': name,
                'link': link,
                'image': imageUrl,
                'set': setName,
                'stock': variantStockList
            }
            stockList.append(results)
            
        self.results = stockList

from bs4 import BeautifulSoup
import requests
import string
from .Scraper import Scraper

# The GauntletScraper URL will only grab in-stock MTG cards
# sorted by cheapest price

class GauntletScraper(Scraper):
    def __init__(self, cardName):
        Scraper.__init__(self, cardName)
        self.baseUrl = 'https://www.gauntletgamesvictoria.ca'
        self.searchUrl = self.baseUrl + '/advanced_search?utf8=%E2%9C%93&search%5Bfuzzy_search%5D=&search%5Btags_name_eq%5D=&search%5Bsell_price_gte%5D=&search%5Bsell_price_lte%5D=&search%5Bbuy_price_gte%5D=&search%5Bbuy_price_lte%5D=&search%5Bin_stock%5D=0&search%5Bin_stock%5D=1&buylist_mode=0&search%5Bcategory_ids_with_descendants%5D%5B%5D=&search%5Bcategory_ids_with_descendants%5D%5B%5D=8&search%5Bwith_descriptor_values%5D%5B6%5D=&search%5Bwith_descriptor_values%5D%5B7%5D=&search%5Bwith_descriptor_values%5D%5B9%5D=&search%5Bwith_descriptor_values%5D%5B10%5D=&search%5Bwith_descriptor_values%5D%5B11%5D=&search%5Bwith_descriptor_values%5D%5B13%5D=&search%5Bwith_descriptor_values%5D%5B348%5D='
        self.url = self.createUrl()

    def createUrl(self):
        url = self.searchUrl
        nameArr = self.cardName.split()
        for word in nameArr:
            url += word
            if word != nameArr[len(nameArr)-1]: # then we don't have last item, add +
                url+= '+' 
            else: url+= '&search%5Bwith_descriptor_values%5D%5B361%5D=&search%5Bwith_descriptor_values%5D%5B1259%5D=&search%5Bwith_descriptor_values%5D%5B17023%5D=&search%5Bwith_descriptor_values%5D%5B17598%5D=&search%5Bwith_descriptor_values%5D%5B17599%5D=&search%5Bwith_descriptor_values%5D%5B17600%5D=&search%5Bwith_descriptor_values%5D%5B17601%5D=&search%5Bwith_descriptor_values%5D%5B17602%5D=&search%5Bwith_descriptor_values%5D%5B17603%5D=&search%5Bwith_descriptor_values%5D%5B17604%5D=&search%5Bwith_descriptor_values%5D%5B17605%5D=&search%5Bwith_descriptor_values%5D%5B17606%5D=&search%5Bwith_descriptor_values%5D%5B17607%5D=&search%5Bwith_descriptor_values%5D%5B17608%5D=&search%5Bwith_descriptor_values%5D%5B17609%5D=&search%5Bvariants_with_identifier%5D%5B14%5D%5B%5D=&search%5Bvariants_with_identifier%5D%5B15%5D%5B%5D=&search%5Bsort%5D=sell_price&search%5Bdirection%5D=ascend&commit=Search&search%5Bcatalog_group_id_eq%5D='
        return url

    def scrape(self):
        page = requests.get(self.url)
 
        sp = BeautifulSoup(page.text, 'html.parser')
        cards = sp.select('li.product div.inner')

        stockList = []

        for card in cards:
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
                'stock': variantStockList,
                'website': 'gauntlet'

            }
            stockList.append(results)
            
        self.results = stockList

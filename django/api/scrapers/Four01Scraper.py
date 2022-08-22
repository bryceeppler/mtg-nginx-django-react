from bs4 import BeautifulSoup
import requests
import string
import json

# This is scraped using an API requests that returns the stock in json
# is nice

class Four01Scraper():
    def __init__(self, cardName):
        self.cardName = cardName
        self.results = []
        self.siteUrl = 'https://store.401games.ca'
        self.baseUrl = 'https://ultimate-dot-acp-magento.appspot.com/full_text_search?request_source=v-next&src=v-next&UUID=d3cae9c0-9d9b-4fe3-ad81-873270df14b5&uuid=d3cae9c0-9d9b-4fe3-ad81-873270df14b5&store_id=17041809&cdn_cache_key=1661088450&api_type=json&facets_required=1&products_per_page=20&narrow=[[%22In+Stock%22,%22True%22],[%22Category%22,%22Magic:+The+Gathering+Singles%22]]&q='
        self.url = self.createUrl()

    def getResults(self):
        return self.results

    def createUrl(self):
        url = self.baseUrl
        nameArr = self.cardName.split()
        for word in nameArr:
            url += word
            if word != nameArr[len(nameArr)-1]: # then we don't have last item, add +
                url+= '+' 
        url += '&page_num=1&sort_by=relevency&with_product_attributes=true'
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
        # make the api request
        responseJson = requests.get(self.url)

        # parse the json response
        data = json.loads(responseJson.content)      

        # create a list to return
        cardList = []

        # get the products
        for item in data['items']:
            name = item['l']
            set = item['v']
            image = item['t']
            url = self.siteUrl + item['u']

            if not self.compareCardNames(self.cardName, name):
                continue 
            
            stock = []
            for stockItem in item['vra']:
                item = stockItem[1]
                if ['Sellable',[False]] in item:
                    continue
                
                if item[0][0] == 'Condition':
                    condition = item[0][1][0]
                    if "NM" in condition:
                        condition="NM"
                    elif "SP" in condition:
                        condition="LP"
                    elif "MP" in condition:
                        condition="MP"
                    elif "Heavy" in condition:
                        condition="HP" 

                    price = float(item[1][1][0].replace("CAD:" , ""))
                    stock.append((condition,price))
                
                elif item[0][0] == 'Price':
                    try:
                        condition = item[3][1][0]
                        if "NM" in condition:
                            condition="NM"
                        elif "SP" in condition:
                            condition="LP"
                        elif "MP" in condition:
                            condition="MP"
                        elif "Heavy" in condition:
                            condition="HP" 

                        price = float(item[0][1][0].replace("CAD:" , ""))
                        stock.append((condition,price))
                    except:
                        pass


            cardList.append({
                'name': name,
                'set': set,
                'image': image,
                'link': url,
                'stock': stock
            })

        self.results = cardList

# if __name__ == '__main__':
#     name = "counterspell"

#     four01Scraper = Four01Scraper(name)
#     four01Scraper.scrape()
#     results = four01Scraper.getResults()
#     print('done')



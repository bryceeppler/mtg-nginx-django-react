from rest_framework.views import APIView
from rest_framework.response import Response
from .scrapers.GauntletScraper import GauntletScraper
from .scrapers.HouseOfCardsScraper import HouseOfCardsScraper
from .scrapers.KanatacgScraper import KanatacgScraper
from .scrapers.FusionScraper import FusionScraper
from .scrapers.Four01Scraper import Four01Scraper
import json
import re
import concurrent.futures

class getPrice(APIView):
    results = []
    def transform(self, scraper):
        scraper.scrape()
        self.results.append(scraper.getResults())
        return 


    def get(self, request):
        # get "name" parameter from request
        name = request.GET.get('name')

        print("Request received with cardName " + name)

        houseOfCardsScraper = HouseOfCardsScraper(name)
        gauntletScraper = GauntletScraper(name)
        kanatacgScraper = KanatacgScraper(name)
        fusionScraper = FusionScraper(name)
        four01Scraper = Four01Scraper(name)

        scrapers = [
            houseOfCardsScraper,
            gauntletScraper,
            kanatacgScraper,
            fusionScraper,
            four01Scraper
        ]

        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            results = executor.map(self.transform, scrapers)
            print(results)

        return Response(self.results)


class getPriceBulk(APIView):

    def post(self, request):
        # get "name" parameter from request
        body = json.loads(request.body.decode('utf-8'))
        data = body['data']

        returnList = []

        numCards = len(data['cards'])
        for card in data['cards']:
            card = re.sub('[0-9]', '', card).lstrip()
            cardStockList = []
            cheapestPrice = 999
            cheapestCard = None

            if data['gauntlet']:
                gauntletScraper = GauntletScraper(card)
                gauntletScraper.scrape()
                gauntletResults = gauntletScraper.getResults()
                if gauntletResults:
                    for cardInfo in gauntletResults:
                        if 'Art Card' in cardInfo['name']:
                            continue
                        for condition, price in cardInfo['stock']:
                            if price < cheapestPrice:
                                cheapestPrice = price
                                cheapestCard = cardInfo
                        cardInfo['website'] = 'gauntlet'
                        cardStockList.append(cardInfo)
            if data['kanatacg']:
                kanatacgScraper = KanatacgScraper(card)
                kanatacgScraper.scrape()
                kanatacgResults = kanatacgScraper.getResults()
                if kanatacgResults:
                    for cardInfo in kanatacgResults:
                        if 'Art Card' in cardInfo['name']:
                            continue
                        for condition, price in cardInfo['stock']:
                            if price < cheapestPrice:
                                cheapestPrice = price
                                cheapestCard = cardInfo
                        cardInfo['website'] = 'kanatacg'
                        cardStockList.append(cardInfo)
            if data['fusion']:
                fusionScraper = FusionScraper(card)
                fusionScraper.scrape()
                fusionResults = fusionScraper.getResults()
                if fusionResults:
                    for cardInfo in fusionResults:
                        if 'Art Card' in cardInfo['name']:
                            continue
                        for condition, price in cardInfo['stock']:
                            if price < cheapestPrice:
                                cheapestPrice = price
                                cheapestCard = cardInfo
                        cardInfo['website'] = 'fusion'
                        cardStockList.append(cardInfo)
            if data['four01']:
                four01Scraper = Four01Scraper(card)
                four01Scraper.scrape()
                four01Results = four01Scraper.getResults()
                if four01Results:
                    for cardInfo in four01Results:
                        for condition, price in cardInfo['stock']:
                            if price < cheapestPrice:
                                cheapestPrice = price
                                cheapestCard = cardInfo
                        cardInfo['website'] = 'four01'
                        cardStockList.append(cardInfo)
            if data['houseOfCards']:
                houseOfCardsScraper = HouseOfCardsScraper(card)
                houseOfCardsScraper.scrape()
                houseOfCardsResults = houseOfCardsScraper.getResults()
                if houseOfCardsResults:
                    for cardInfo in houseOfCardsResults:
                        if 'Art Card' in cardInfo['name']:
                            continue
                        for condition, price in cardInfo['stock']:
                            if price < cheapestPrice:
                                cheapestPrice = price
                                cheapestCard = cardInfo
                            else:
                                continue

                        cardInfo['website'] = 'houseOfCards'
                        cardStockList.append(cardInfo)

            for card in cardStockList:
                if ('Art Card' in card['name']):
                    continue
                for stock in card['stock']:
                    price = stock[1]
                    if price < cheapestPrice:
                        cheapestPrice = price
                        cheapestCard = card
                        cheapestCard['stock'] = stock

            returnList.append(cheapestCard)

        numCardsFound = len(returnList)

        results = {
            "status": str(numCardsFound) + " / " + str(numCards) + " cards found",
            'results': returnList
        }
        return Response(results)

from rest_framework.views import APIView
from rest_framework.response import Response
from .scrapers.GauntletScraper import GauntletScraper
from .scrapers.HouseOfCardsScraper import HouseOfCardsScraper
from .scrapers.KanatacgScraper import KanatacgScraper
from .scrapers.FaceToFaceScraper import FaceToFaceScraper
from .scrapers.FusionScraper import FusionScraper
from .scrapers.Four01Scraper import Four01Scraper
import json


class getPrice(APIView):

    def get(self, request):
        # get "name" parameter from request
        name = request.GET.get('name')

        print("Request received with cardName " + name)

        houseOfCardsScraper = HouseOfCardsScraper(name)
        gauntletScraper = GauntletScraper(name)
        kanatacgScraper = KanatacgScraper(name)
        faceToFaceScraper = FaceToFaceScraper(name)
        fusionScraper = FusionScraper(name)
        four01Scraper = Four01Scraper(name)

        print('Scraping HouseOfCards')
        houseOfCardsScraper.scrape()
        print('Scraping Gauntlet')
        gauntletScraper.scrape()
        print('Scraping Kanatacg')
        kanatacgScraper.scrape()
        print('Scraping FaceToFace')
        faceToFaceScraper.scrape()
        print('Scraping Fusion')
        fusionScraper.scrape()
        print('Scraping Four01')
        four01Scraper.scrape()

        print('Retreiving HouseOfCards data')
        houseOfCardsResults = houseOfCardsScraper.getResults()
        print('Retreiving Gauntlet data')
        gauntletResults = gauntletScraper.getResults()
        print('Retreiving Kanatacg data')
        kanatacgResults = kanatacgScraper.getResults()
        print('Retreiving FaceToFace data')
        faceToFaceResults = faceToFaceScraper.getResults()
        print('Retreiving Fusion data')
        fusionResults = fusionScraper.getResults()
        print('Retreiving Four01 data')
        four01Results = four01Scraper.getResults()

        print('Merging results')
        results = {
            'houseOfCards': houseOfCardsResults,
            'gauntlet': gauntletResults,
            'kanatacg': kanatacgResults,
            'faceToFace': faceToFaceResults,
            'fusion': fusionResults,
            'four01': four01Results
        }

        return Response(results)


class getPriceBulk(APIView):

    def post(self, request):
        # get "name" parameter from request
        body = json.loads(request.body.decode('utf-8'))
        data = body['data']

        returnList = []

        numCards = len(data['cards'])
        for card in data['cards']:
            cardStockList = []
            if data['gauntlet']:
                gauntletScraper = GauntletScraper(card)
                gauntletScraper.scrape()
                gauntletResults = gauntletScraper.getResults()
                if gauntletResults:
                    for cardInfo in gauntletResults:
                        cardInfo['website'] = 'gauntlet'
                        cardStockList.append(cardInfo)
            if data['kanatacg']:
                print(card)
                kanatacgScraper = KanatacgScraper(card)
                kanatacgScraper.scrape()
                kanatacgResults = kanatacgScraper.getResults()
                if kanatacgResults:
                    for cardInfo in kanatacgResults:
                        cardInfo['website'] = 'kanatacg'
                        cardStockList.append(cardInfo)
            if data['fusion']:
                fusionScraper = FusionScraper(card)
                fusionScraper.scrape()
                fusionResults = fusionScraper.getResults()
                if fusionResults:
                    for cardInfo in fusionResults:
                        cardInfo['website'] = 'fusion'
                        cardStockList.append(cardInfo)
            if data['four01']:
                four01Scraper = Four01Scraper(card)
                four01Scraper.scrape()
                four01Results = four01Scraper.getResults()
                if four01Results:
                    for cardInfo in four01Results:
                        cardInfo['website'] = 'four01'
                        cardStockList.append(cardInfo)
            if data['houseOfCards']:
                houseOfCardsScraper = HouseOfCardsScraper(card)
                houseOfCardsScraper.scrape()
                houseOfCardsResults = houseOfCardsScraper.getResults()
                if houseOfCardsResults:
                    for cardInfo in houseOfCardsResults:
                        cardInfo['website'] = 'houseOfCards'
                        cardStockList.append(cardInfo)

            cheapestPrice = 999
            cheapestCard = None
            for card in cardStockList:
                for stock in card['stock']:
                    price = stock[1]
                    if price < cheapestPrice:
                        cheapestPrice = price
                        cheapestCard = card
                        cheapestCard['stock'] = stock
            # print(cheapestCard)
            returnList.append(cheapestCard)

        numCardsFound = len(returnList)

        results = {
            "status": str(numCardsFound) + " / " + str(numCards) + " cards found",
            'results': returnList
        }
        return Response(results)

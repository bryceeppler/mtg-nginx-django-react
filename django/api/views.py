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








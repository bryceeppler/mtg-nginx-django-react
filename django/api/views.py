from rest_framework.views import APIView
from rest_framework.response import Response
from .scrapers.GauntletScraper import GauntletScraper
from .scrapers.HouseOfCardsScraper import HouseOfCardsScraper
from .scrapers.KanatacgScraper import KanatacgScraper


class getPrice(APIView):

    def get(self, request):
        # get "name" parameter from request
        name = request.GET.get('name')

        print("Request received with cardName " + name)

        print('Creating HouseOfCardsScraper')
        houseOfCardsScraper = HouseOfCardsScraper(name)
        print('Creating GauntletScraper')
        gauntletScraper = GauntletScraper(name)
        print('Creating KanatacgScraper')
        kanatacgScraper = KanatacgScraper(name)

        print('Scraping HouseOfCards')
        houseOfCardsScraper.scrape()
        print('Scraping Gauntlet')
        gauntletScraper.scrape()
        print('Scraping Kanatacg')
        kanatacgScraper.scrape()

        print('Retreiving HouseOfCards data')
        houseOfCardsResults = houseOfCardsScraper.getResults()
        print('Retreiving Gauntlet data')
        gauntletResults = gauntletScraper.getResults()
        print('Retreiving Kanatacg data')
        kanatacgResults = kanatacgScraper.getResults()

        print('Merging results')
        results = {
            'houseOfCards': houseOfCardsResults,
            'gauntlet': gauntletResults,
            'kanatacg': kanatacgResults
        }

        return Response(results)








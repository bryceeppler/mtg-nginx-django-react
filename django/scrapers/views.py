from rest_framework.views import APIView
from rest_framework.response import Response
from .scrapers.GauntletScraper import GauntletScraper
from .scrapers.HouseOfCardsScraper import HouseOfCardsScraper
from .scrapers.KanatacgScraper import KanatacgScraper
from .scrapers.FusionScraper import FusionScraper
from .scrapers.Four01Scraper import Four01Scraper
import json
import re

# Create your views here.
class GauntletList(APIView):
    def get(self, request):
        """
        Return all listings for a given card name
        """
        name = request.GET.get('name')
        gauntletScraper = GauntletScraper(name)
        gauntletScraper.scrape()
        gauntletResults = gauntletScraper.getResults()
        return Response(gauntletResults)

class HouseOfCardsList(APIView):
    def get(self, request):
        """
        Return all listings for a given card name
        """
        name = request.GET.get('name')
        houseOfCardsScraper = HouseOfCardsScraper(name)
        houseOfCardsScraper.scrape()
        houseOfCardsResults = houseOfCardsScraper.getResults()
        return Response(houseOfCardsResults)


class KanatacgList(APIView):
    def get(self, request):
        """
        Return all listings for a given card name
        """
        name = request.GET.get('name')
        kanatacgScraper = KanatacgScraper(name)
        kanatacgScraper.scrape()
        kanatacgResults = kanatacgScraper.getResults()

class FusionList(APIView):
    def get(self, request):
        """
        Return all listings for a given card name
        """
        name = request.GET.get('name')
        fusionScraper = FusionScraper(name)
        fusionScraper.scrape()
        fusionResults = fusionScraper.getResults()


class Four01List(APIView):
    def get(self, request):
        """
        Return all listings for a given card name
        """
        name = request.GET.get('name')
        four01Scraper = Four01Scraper(name)
        four01Scraper.scrape()
        four01Results = four01Scraper.getResults()
        return Response(four01Results)



class GauntletCheapest(APIView):
    def get(self, request):
        """
        Return the cheapest listing for a given card name
        """
        name = request.GET.get('name')

        pass

class HouseOfCardsCheapest(APIView):
    def get(self, request):
        """
        Return the cheapest listing for a given card name
        """
        name = request.GET.get('name')

        pass

class KanatacgCheapest(APIView):
    def get(self, request):
        """
        Return the cheapest listing for a given card name
        """
        name = request.GET.get('name')

        pass

class FusionCheapest(APIView):
    def get(self, request):
        """
        Return the cheapest listing for a given card name
        """
        name = request.GET.get('name')

        pass

class Four01Cheapest(APIView):
    def get(self, request):
        """
        Return the cheapest listing for a given card name
        """
        name = request.GET.get('name')

        pass
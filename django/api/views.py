from rest_framework.views import APIView
from rest_framework.response import Response
from .scrapers.HouseOfCards import HouseOfCardsSpider
from .scrapers.Gauntlet import GauntletSpider
from .scrapers.WT import WTSpider
from .utils.UrlGenerator import UrlGenerator


class getPrice(APIView):

    def get(self, request):
        # get "name" parameter from request
        name = request.GET.get('name')

        # generate urls
        urlGenerator = UrlGenerator(name)
        
        # scrape house of cards and return reponse
        hocSpider = HouseOfCardsSpider(name, urlGenerator.hocUrl)
        gauntletSpider = GauntletSpider(name, urlGenerator.gauntletUrl)
        wtSpider = WTSpider(name, urlGenerator.wtUrl)
    
    
        return Response({
            'House of Cards': hocSpider.getStock(),
            'Gauntlet Games': gauntletSpider.getStock(),
            'Wizards Tower': wtSpider.getStock()
        })








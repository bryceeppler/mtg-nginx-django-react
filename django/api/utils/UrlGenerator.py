class UrlGenerator():
    def __init__(self, cardName):
        self.cardName=cardName
        self.hocUrl = self.createHOCUrl(cardName)
        self.gauntletUrl = self.createGauntletUrl(cardName)
        self.wtUrl = self.createWTUrl(cardName)

    def createHOCUrl(self, cardName):
        baseUrl = 'https://houseofcards.ca/search?page=1&q=%2A'
        nameArr = cardName.split()
        for word in nameArr:
            baseUrl += word
            if word != nameArr[len(nameArr)-1]: # then we don't have last item, add %20
                baseUrl+= '%20' 
            else: baseUrl+= '%2A'
        return baseUrl

    def createGauntletUrl(self, cardName):
        baseUrl = 'https://www.gauntletgamesvictoria.ca/products/search?q='
        nameArr = cardName.split()
        for word in nameArr:
            baseUrl += word
            if word != nameArr[len(nameArr)-1]: # then we don't have last item, add +
                baseUrl+= '+' 
            else: baseUrl+= '&c1'
        return baseUrl

    def createWTUrl(self, cardName):
        baseUrl='https://www.kanatacg.com/products/search?query='
        nameArr = cardName.split()
        for word in nameArr:
            baseUrl +=word
            if word != nameArr[len(nameArr)-1]: # then we don't have last item, add +
                baseUrl+= '+'
            else: pass
        return baseUrl
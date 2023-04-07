class PassagemScraper():
    def __init__(self, url):
        self.__url = url

    def setUrl(self, url: str):
        self.__url = url

    def getUrl(self):
        return self.__url
    
    def visitSite(self, browser):
        try: 
            print('Visitando: ' + self.__url)
            browser.visit(self.__url)
        except:
            print("URL inválido!")
            return False
        return True
    

from splinter import Browser
from sites import PassagemScraper
from classes import filtrosPesquisa

class Decolar(PassagemScraper):
    def __init__(self):
        super().__init__("https://www.decolar.com/shop/flights/results")

    def makeUrl(self, filtros : filtrosPesquisa):
        url = self.getUrl()
        ida = filtros.getDataIda()

        if (filtros.getTipoViagem() == 'roundtrip'):
            volta = filtros.getDataVolta()
            url += f'/{filtros.getTipoViagem()}/{filtros.origem}/{filtros.destino}/{ida}/{volta}/1/0/0/NA/NA/NA/NA/NA?from=SB&di=1-0'
        elif (filtros.getTipoViagem() == 'oneway'):
            url += f'/{filtros.getTipoViagem()}/{filtros.origem}/{filtros.destino}/{ida}/1/0/0/NA/NA/NA/NA?from=SB&di=1-0'
       
        self.setUrl(url)
        return

    def rasparDados(self, browser: Browser):

        if (not self.visitSite(browser)):
            return False

        cluster = browser.find_by_tag('cluster')
        precos = browser.find_by_xpath('//fare/span/span')

        resultados = []
        passagens = []
        for cont in range(0, len(cluster)):
    
            precos[cont].value.split('\n')[-2].split('$')[1]
            precoFinal = precos[cont].value.split('\n')[-2].split('$')[1]

            routeChoice = cluster[cont].find_by_tag('route-choice')

            voosIda = voosVolta = None
            voosIda = self.getViagensInfo(routeChoice[0],precoFinal)

            if (len(routeChoice) > 1):
                voosVolta = self.getViagensInfo(routeChoice[1],precoFinal)

            resultados.append({'VoosIda': voosIda, 'VoosVolta': voosVolta})
        print(resultados)
        return resultados

    def getViagensInfo(self, routeChoice, preco): 
        lines = routeChoice.find_by_tag('li')
        voos = []

        for line in lines:  
          if (line.text != ''):
               companhia = line.find_by_css('.name').text
               horaVoo = line.find_by_css('.leave').text
               paradas = line.find_by_css('.stops-text').text.split(' ') 
               duracao = line.find_by_css('.time').text
               previsaoChegada = line.find_by_css('.arrive').text.split('\n')[0]

               voos.append({"companhia":companhia, "horaVoo": horaVoo, "paradas": paradas[0], "duracao":duracao, "previsaoChegada": previsaoChegada, "preco":preco})
        return voos
from splinter import Browser
from sites import PassagemScraper
from classes import filtrosPesquisa
import json

class Decolar(PassagemScraper):
    def __init__(self):
        super().__init__("https://www.decolar.com/shop/flights/results")

    def makeUrl(self, filtros : filtrosPesquisa):
        url = self.getUrl()
        ida = filtros.getDataIda().strftime("%Y-%m-%d")

        if (filtros.getTipoViagem() == 'roundtrip'):
            volta = filtros.getDataVolta().strftime("%Y-%m-%d")
            url += f'/{filtros.getTipoViagem()}/{filtros.origem}/{filtros.destino}/{ida}/{volta}/1/0/0/NA/NA/NA/NA/NA?from=SB&di=1-0'
        else:
            url += f'/{filtros.getTipoViagem()}/{filtros.origem}/{filtros.destino}/{ida}/1/0/0/NA/NA/NA/NA?from=SB&di=1-0'
       
        self.setUrl(url)

    def rasparDados(self, browser: Browser):

        if (not self.visitSite(browser)):
            return False
        
        cluster = browser.find_by_css('.COMMON .cluster-container')
        resultados = []

        for opcoes in cluster:
            companhia = horaVoo = paradas = moeda = precoFinal = duracao = previsaoChegada = None 
            lines = opcoes.find_by_css('.itinerary-wrapper')

            for line in lines:     
                try:
                    companhia = line.find_by_css('.airline-container .name').text
                except:
                    companhia = None

                try: 
                    horaVoo = line.find_by_css('.leave').text
                except:
                    horaVoo = None      
                
                try:
                    paradas = line.find_by_css('.stops-text').text.split(' ') 
                except:
                    paradas = None

                try:
                    duracao = line.find_by_css('.time').text 
                except:
                    duracao = None

                try:
                    previsaoChegada = line.find_by_css('.arrive').text.split('\n')[0] 
                except:
                    previsaoChegada = None

                try: 
                    priceLabel = opcoes.find_by_css('.fare-price .flight-price-label')
                    if (priceLabel.is_empty()):
                        priceLabel = opcoes.find_by_css('.flight-price-label')
    
                    moeda, precoFinal = priceLabel.text.split('$')
                except:
                    priceLabel = None
                     

                resultados.append({"companhia":companhia, 
                                    "vooIda": {
                                        "horaVoo": horaVoo, 
                                        'paradas': paradas[0], 
                                        "duracao":duracao, 
                                        "previsaoChegada": previsaoChegada
                                    },
                                    "vooVolta": None,
                                    "moeda": str(moeda)+'$' if moeda != None else moeda, 
                                    "precoFinal": precoFinal})

        json_object = json.dumps(resultados, indent = 4) 
        with open("./data/resultados.json", "w") as outfile: 
            outfile.write(json_object)  
            outfile.close()

        return True

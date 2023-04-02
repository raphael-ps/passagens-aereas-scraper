from splinter import Browser

import json

class PassagemScraper():
    def __init__(self, url):
        self.url = url

    def visitSite(self, browser):
        try: 
            browser.visit(self.url)
        except:
            print("URL inválido!")
            return False
        return True
    
class Decolar(PassagemScraper):
    def __init__(self, url):
        super().__init__(url)

    def rasparDados(self, browser: Browser):

        if (not self.visitSite(browser)):
            return False
        
        cluster = browser.find_by_css('.COMMON .cluster-container')
        resultados = []

        for opcoes in cluster:
            line = opcoes.find_by_css('.itinerary-wrapper')

            companhia = line[0].find_by_css('.airline-container .name').text
            horaVoo = line.find_by_css('.leave').text
            paradas = line.find_by_css('.stops-text').text.split(' ') 
            duracao = line.find_by_css('.time').text 
            previsaoChegada = line.find_by_css('.arrive').text 
            priceLabel = opcoes.find_by_css('.fare-price .flight-price-label')[0].text
            moeda = priceLabel[:2]
            precoFinal = priceLabel[2:]

            resultados.append({"companhia":companhia, 
                               "horaVoo": horaVoo, 
                               'paradas': paradas[0], 
                               "duracao":duracao, 
                               "previsaoChegada": previsaoChegada, 
                               "moeda": moeda, 
                               "precoFinal": precoFinal})

        json_object = json.dumps(resultados, indent = 4) 
        with open("resultados.json", "w") as outfile: 
            outfile.write(json_object)  
            outfile.close()

        return True

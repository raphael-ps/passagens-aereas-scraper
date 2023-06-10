from splinter import Browser
from sites import Decolar
from classes import filtrosPesquisa
import json 



#https://www.decolar.com/shop/flights/results/roundtrip/SAO/FOR/2023-05-27/2023-06-27/1/0/0/NA/NA/NA/NA/NA?from=SB&di=1-0

browser = Browser('edge', headless=True, incognito=True)
browser.driver.set_window_size(1000, 600)

pesquisa = filtrosPesquisa()
pesquisa.setTipoViagem('oneway')
pesquisa.setDataIda('27/07/2023')
pesquisa.setDataVolta('27/08/2023')

# with open('./data/aeroportos.json', 'r') as data:
#     aeroportos = json.load(data)
#     pesquisa.origem = aeroportos['fortaleza'][0]['iata']
#     pesquisa.destino = aeroportos['orlando'][0]['iata']
pesquisa.origem = 'FOR'
pesquisa.destino = 'RIO'

scraperDecolar = Decolar()
scraperDecolar.makeUrl(pesquisa)
data = scraperDecolar.rasparDados(browser)

with open('./data/resultados.json', 'w+') as file:
    file.write(data)




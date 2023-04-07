from splinter import Browser
from sites import Decolar
from classes import filtrosPesquisa
import json 

browser = Browser('edge', headless=True,incognito=True)
browser.driver.set_window_size(1000, 600)

pesquisa = filtrosPesquisa()
pesquisa.setTipoViagem('oneway')
pesquisa.setDataIda('29/04/2023')
pesquisa.setDataVolta('30/05/2023')

with open('./data/aeroportos.json', 'r') as data:
    aeroportos = json.load(data)
    pesquisa.origem = aeroportos['fortaleza'][0]['iata']
    pesquisa.destino = aeroportos['orlando'][0]['iata']

scraperDecolar = Decolar()
scraperDecolar.makeUrl(pesquisa)

if (scraperDecolar.rasparDados(browser)): 
    print("Teste Ok")
else:
    print("Teste não OK")
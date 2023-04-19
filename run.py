from splinter import Browser
from flask import Flask, request
from sites import Decolar
from classes import filtrosPesquisa
import json 

app = Flask(__name__)

@app.route('/scraping')
def scraping():
    origem = request.args.get('origem')
    destino = request.args.get('destino')
    tipo = request.args.get('tipo')
    ida = request.args.get('ida')
    volta = request.args.get('volta')

    browser = Browser('edge', headless=True,incognito=True)
    browser.driver.set_window_size(1000, 600)

    pesquisa = filtrosPesquisa()
    pesquisa.setTipoViagem(tipo)
    pesquisa.setDataIda(ida)
    pesquisa.setDataVolta(volta)

    # with open('./data/aeroportos.json', 'r') as data:
    #     aeroportos = json.load(data)
    #     pesquisa.origem = aeroportos['fortaleza'][0]['iata']
    #     pesquisa.destino = aeroportos['orlando'][0]['iata']
    pesquisa.origem = origem
    pesquisa.destino = destino

    scraperDecolar = Decolar()
    scraperDecolar.makeUrl(pesquisa)
    data = scraperDecolar.rasparDados(browser)
    if (data): 
        return data
    else:
        return "[]"



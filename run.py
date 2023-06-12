from splinter import Browser
from flask import Flask, request, redirect, render_template
from sites import Decolar
from classes import filtrosPesquisa

app = Flask(__name__)

@app.route('/passagens', methods = ['POST'])
def scraping():
    if request.method == 'POST':
        origem = request.form.get('origem')
        destino = request.form.get('destino')
        ida = request.form.get('ida')
        volta = request.form.get('volta')
        tipo = "oneway"
        if ida and volta:
            tipo = "roundtrip"
        browser = Browser('edge', headless=True, incognito=True)
        browser.driver.set_window_size(1000, 600)

        pesquisa = filtrosPesquisa()
        pesquisa.setTipoViagem(tipo)
        pesquisa.setDataIda(ida)
        pesquisa.setDataVolta(volta)

        pesquisa.origem = origem
        pesquisa.destino = destino

        scraperDecolar = Decolar()
        scraperDecolar.makeUrl(pesquisa)
        data = scraperDecolar.rasparDados(browser)
        if (data): 
            return render_template("viagem.html", data=data)
        else:
            return redirect('http://localhost/BooKariri/home.html',302)



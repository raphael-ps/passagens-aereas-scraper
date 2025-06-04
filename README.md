# passagens-aereas-scraper

Este projeto é um raspador de dados feito em python com a biblioteca Splinter, feito para a
disciplina de engenharia de software, sob medida para o site da Decolar. O programa recebe
informações de data, origem e destino de voos, raspa as informações sobre os voos
disponíveis no site da decolar e responde com um conjunto de voos disponíveis.
(Descontinuado)

## Testando Coisas
### Comando para executar a aplicação
```base
flask --app run run
```
### Exemplo de get, utilizando postman ou similares
```bash
http://127.0.0.1:5000/scraping?origem=FOR&destino=SFB&tipo=oneway&ida=29/04/2023&volta=30/05/2023
```

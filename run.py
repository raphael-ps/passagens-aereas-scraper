from splinter import Browser
from passagensScraper import Decolar

url = 'https://www.decolar.com/shop/flights/results/oneway/FOR/GRU/2023-04-08/1/0/0/NA/NA/NA/NA?from=SB&di=1-0'
browser = Browser('edge', headless=True,incognito=True)
browser.driver.set_window_size(1000, 600)

scraperDecolar = Decolar(url)

if (scraperDecolar.rasparDados(browser)): 
    print("Teste Ok")
else:
    print("Teste não OK")
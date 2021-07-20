from os import write
import pandas as pd
from selenium import webdriver
from time import sleep
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

options = Options()
options.headless = True

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

with open ('class.txt') as links:
    for line in links:
        driver.get(line)
      
        sleep(2)
        try:
            url = driver.current_url
            print("Link: ",url)
        except:
            print("URL não encontrada")
        
        try:
            produto = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[1]/span').text
            sleep(2)
            print("Nome Produto:",produto)
        except:
            print("Produto não encontrado")
        try:
            de_valor = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[3]/div/div/div/div/div[1]').text
            sleep(2)
            print("De R$",de_valor)
        except:
            print("De valor não encontrado")
        else:
            de_valor = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[3]/div/div/div/div/div/div').text
            print("Valor R$",de_valor)
            
        try:
            por_valor = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[3]/div/div/div/div/div[2]/div[1]').text
            sleep(2)
            print("Por R$",por_valor)
        except:
            print("Por valor não encontrado")
        else:
            por_valor = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[3]/div/div/div/div/div/div').text
            
        try:
            vendedor = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[1]').text
            sleep(2)
            print("Nome Vendedor: ",vendedor)
        except:
            print("Vendedor não encontrado")
            
        try:
            estado = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div').text
            sleep(2)
            print("Estado: ",estado)
        except:
            print("Estado não encontrado")
            
        try:
            estoque = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div').text
            sleep(2)
            print("Estoque: ",estoque)
        except:
            print("Estoque não encontrado")
        
        print('\n')           

    driver.quit()

    


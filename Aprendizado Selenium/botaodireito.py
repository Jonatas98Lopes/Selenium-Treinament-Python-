from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import  ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep
from random import randint

def iniciar_drive():
    chrome_options = Options()
    arguments = ['--lang=pt-BR','--window-size=900,900','--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)
    
    chrome_options.add_experimental_option('prefs',{
       'download.prompt_for_download': False,
       'profile.default_content_setting_values.notifications': 2,
       'profile.default_content_setting_values.automatic_downloads': 1 
    })
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    return driver

def digitar_naturalmente(texto, elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(randint(1,5)/30)

def esperar_naturalmente():
    sleep(randint(10,30))

driver = iniciar_drive()
sleep(2)
driver.get('https://cursoautomacao.netlify.app/exemplo_chains')
sleep(2)
botao_direito = driver.find_element(By.ID, 'botao-direito')
sleep(2)
chain = ActionChains(driver)
sleep(2)
chain.context_click(botao_direito).pause(3)
for x in range(3):
    chain.send_keys(Keys.ARROW_DOWN).pause(3).perform()
chain.send_keys(Keys.ENTER).perform()
sleep(2)
alerta = driver.switch_to.alert
sleep(2)
alerta.dismiss()
sleep(2)
voltar = driver.find_element(By.LINK_TEXT,'Dev Aprender')
sleep(2)
voltar.click()
input()
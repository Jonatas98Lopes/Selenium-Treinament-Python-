from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import  ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from random import randint

def iniciar_drive():
    chrome_options = Options()
    arguments = ['--lang=pt-BR','--window-size=900,800','--incognito']
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
sleep(0.8)
driver.get('https://cursoautomacao.netlify.app/')
sleep(0.8)
driver.execute_script('window.scrollTo(100, 600);')
sleep(0.8)
pergunta = driver.find_element(By.ID,"botaoPrompt")
sleep(0.8)
pergunta.click()
sleep(0.8)
alerta = driver.switch_to.alert
sleep(0.8)
alerta.send_keys("Dia dezessete de fevereiro de dois mil e vinte e três.")
alerta.accept()
sleep(0.8)
alerta.dismiss()
input()
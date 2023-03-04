from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options # Gerenciar opções do chrome, como resolução e linguagem do site.
from selenium.webdriver.common.by import BY
"""
# Fonte de opções de switches https://chromium.googlesource.com/chromium/src/+/master/chrome/common/chrome_switches.cc e  https://peter.sh/experiments/chromium-command-line-switches/

Opções de configuração de Options
 --start-maximized # Inicia na resolução máxima da janela.
--lang =pt-BR # Define o idioma de inicialização: en-Us, pt-BR
--Incognito # Usar o modo anônimo 
--window-size=800, 800 # Defina a resolução da janela em largura e altura
--headless # Roda em segundo plano(com a janela fechada)
--disable-notifications #Desabilita notificações
--disable-gpu #Desabilita renderização com GPU
 """
chrome_options = Options()
arguments = ['--lang=pt-BR', '--window-size=500,500', '--incognito']
for argument in arguments:
    chrome_options.add_argument(argument)

# Lista de opções experimentais(nem todas estão documentadas) https://chromium.googlesource.com/chromium/src/+/master/chrome/common/pref_names.cc
# Uso de configurações experimentais
chrome_options.add_experimental_option('prefs', {
    # Alterar o local padrão de download de arquivos
    'download.default_directory': 'C:\\Users\\jonat\\OneDrive\\Área de Trabalho\\Automatizações com selenium\\Aprendizado Selenium\\downloads',
    # notificar o google chrome sobre essa alteração
    'download.directory_upgrade': True,
    # Desabilitar a confirmação de download
    'download.prompt_for_download': False,
    # Desabilitar notificações
    'profile.default_content_setting_values.notifications': 2,
    # Permitir multiplos downloads
    'profile.default_content_setting_values.automatic_downloads': 1,

})
from tkinter import Radiobutton
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=800,600', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    return driver


driver = iniciar_driver()
driver.get('https://cursoautomacao.netlify.app/')

# tag(section,div,h4,button)
# class(.btn)
# combinação de class(.btn.btn-success)
# Id (#dropDownMenuButton)

# Para encontrar valores exatos
# input[class='form-check-input']
# Inicia com algum valor
# input[class^='form']
# finaliza com algum valor
# input[class$='input']
# Contem algum valor
# input[class*='check']

elemento_h2 = driver.find_element(By.CSS_SELECTOR,'h2')
elementos_form_chec = driver.find_element(By.CSS_SELECTOR,'input[class="form-check-input"]')

input('')
driver.close()
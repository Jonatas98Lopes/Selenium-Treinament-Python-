from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep


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
""" 
botao = driver.find_element(By.ID,'btn1')
botao = driver.find_element(By.NAME,'estenome')
botao = driver.find_element(By.CLASS_NAME,'nomedaclasse')
botao = driver.find_element(By.LINK_TEXT,'Home')
botao = driver.find_element(By.PARTIAL_LINK_TEXT'Ho')
botao = driver.find_element(By.XPATH,'//*[text()="ZONA DE TESTE"]')
botao = driver.find_element(By.TAG_NAME,'h1')
botao = driver.find_element(By.XPATH,'//h5[@class="atributo"]')
 """
input('digite algo para fechar... ')
""" sleep(3)
driver.execute_script('window.scrollTo(0, document.body.scrollHeight)') 
sleep(3)
driver.execute_script('window.scrollTo(0, document.body.scrollTop)') 
sleep(5) """
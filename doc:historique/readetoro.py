from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Remplacez les variables ci-dessous par vos informations
url = 'https://www.etoro.com/home'
username = 'your_username'
password = 'your_password'
target_url = 'https://www.etoro.com/portfolio/overview'

# Chemin vers le WebDriver (par exemple, ChromeDriver)
webdriver_path = 'C:/Applications/Google Chrome.app'

# Initialiser le navigateur


driver = webdriver.Chrome()
driver.get(url)

'''
service = Service(executable_path=webdriver_path)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
'''

try:
    # Accéder à la page de connexion
    driver.get(url)


    time.sleep(60)
    '''
    
    # Attendre que la case reCAPTCHA soit présente et essayer de la cocher
    WebDriverWait(driver, 20).until(
        EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[src*='recaptcha']"))
    )

    # Cliquer sur la case reCAPTCHA
    captcha_box = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div.recaptcha-checkbox-border"))
    )
    captcha_box.click()

    # Revenir au contexte principal après avoir interagi avec le CAPTCHA
    driver.switch_to.default_content()
    '''

    '''
    # Attendre que le champ du nom d'utilisateur soit présent
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'username'))
    )

    # Entrer le nom d'utilisateur
    username_field = driver.find_element(By.NAME, 'username')
    username_field.send_keys(username)

    # Entrer le mot de passe
    password_field = driver.find_element(By.NAME, 'password')
    password_field.send_keys(password)

    # Soumettre le formulaire de connexion
    password_field.send_keys(Keys.RETURN)

    # Attendre que la page suivante soit chargée
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'body'))
    )

    # Naviguer vers une page cible après la connexion
    driver.get(target_url)

    # Effectuer une tâche sur la page cible (par exemple, récupérer du texte)
    target_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'target_element_id'))
    )
    print(target_element.text)
    '''

    # Laisser la page ouverte pendant 5 minutes (300 secondes)
    time.sleep(300)

finally:
    # Fermer le navigateur
    driver.quit()

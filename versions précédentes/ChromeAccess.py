import selenium
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

c = webdriver.ChromeOptions()
#incognito parameter passed
c.add_argument("--incognito")
#set chromodriver.exe path
driver = webdriver.Chrome(ChromeDriverManager().install(), options=c)
#driver.implicitly_wait(0.5)
#launch URL
driver.get("https://www.etoro.com/fr/login")
# Using Chrome to access web
##driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Chrome("C:/Users/macbookpro/.wdm/drivers/chromedriver/mac64/94.0.4606.61/chromedriver")
# Open the website
##driver.get('https://www.etoro.com/fr/login')
id_box = driver.find_element(By.ID, 'username')
id_box.send_keys('Pyrithe')

# Find password box
pass_box = driver.find_element(By.ID, 'password')
# Send password
pass_box.send_keys('Arbiter01')

# Find login button
login_button = driver.find_element(By.TAG_NAME, 'button')
# Click login
login_button.click()
time.sleep(2000)

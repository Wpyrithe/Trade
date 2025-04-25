import selenium
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Chrome("C:/Users/macbookpro/.wdm/drivers/chromedriver/mac64/94.0.4606.61/chromedriver")
# Open the website
driver.get('https://www.etoro.com/home')

#id_box = driver.find_element(By.XPATH, 'nav/ul/li[3]')
#id_box.click()
time.sleep(200)
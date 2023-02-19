import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()
driver.get("https://www.facebook.com")

print("Application tittle is : ",driver.title)
print("Application URL is : ",driver.current_url)

login_button = driver.find_element(By.NAME, 'login').click()
time.sleep(5)

driver.close()
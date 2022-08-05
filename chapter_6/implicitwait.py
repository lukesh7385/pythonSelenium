import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Program Files\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.google.com/")
driver.minimize_window()

searchbox = driver.find_element(By.NAME, "q")

searchbox.send_keys("selenium")
searchbox.submit()

# time.sleep(5)
driver.find_element(By.XPATH, "//a[@href='https://www.selenium.dev/']//h3").click()

driver.quit()



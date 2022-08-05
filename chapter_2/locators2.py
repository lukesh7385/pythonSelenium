from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Program Files\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("http://automationpractice.com/")
driver.maximize_window()

sliders = driver.find_elements(By.CLASS_NAME, 'homeslider-container')
print(len(sliders)) #5

Link = driver.find_elements(By.TAG_NAME, 'a')
print(len(Link)) # 149 total number of links on home page



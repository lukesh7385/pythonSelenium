from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Program Files\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensorce-demo.orangehrmlive.com/")
driver.get("https://www.snapdeal.com/")
driver.maximize_window()

driver.back()
driver.forward()
driver.refresh()
driver.quit()
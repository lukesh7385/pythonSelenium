import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Program Files\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()

button = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")

act = ActionChains(driver)
act.context_click(button).perform()  # Right click

time.sleep(5)
driver.find_element(By.XPATH, "//span[normalize-space()='Copy']").click()
time.sleep(3)
driver.switch_to.alert.accept()

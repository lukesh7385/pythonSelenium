import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Program Files\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

#  open alerts window
driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']").click()
time.sleep(5)

alertwindow = driver.switch_to.alert

print(alertwindow.text)
alertwindow.send_keys("welcome")

# alertwindow.accept()  # closed alert window by using ok button
alertwindow.dismiss()  # closed alert window by using ok button

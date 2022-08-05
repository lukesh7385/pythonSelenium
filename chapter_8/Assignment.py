import link as link
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import switch_to
from selenium.webdriver.remote.webelement import WebElement

serv_obj = Service("C:\Program Files\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

parentwindowid = driver.find_element(By.XPATH, "//input[@id='Wikipedia1_wikipedia-search-input']")
parentwindowid.send_keys("selenium")
driver.find_element(By.XPATH, "//*[@id='Wikipedia1_wikipedia-search-form']/div/span[2]/span[2]/input").click()

Totallinks = driver.find_elements(By.XPATH, "//div[@id='Wikipedia1_wikipedia-search-results']//div")

count = 0
for r in range(1, Totallinks + 1):
    status = driver.find_elements(By.XPATH, "//div[@id='Wikipedia1_wikipedia-search-results']//div["+str(r)+"]").text
    if status == "Enabled":
        count = count + 1





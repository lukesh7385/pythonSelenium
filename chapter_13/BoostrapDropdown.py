from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\Program Files\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.XPATH, "//span[@id='select2-billing_country-container']").click()

countreslist = driver.find_elements(By.XPATH, "//ul[@id='select2-billing_country-results']/li")
print(len(countreslist))

for c in countreslist:
    if c.text == "India":
        c.click()
        break

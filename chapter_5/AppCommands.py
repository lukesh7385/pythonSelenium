from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\Program Files\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://opensorce-demo.orangehrmlive.com/")
driver.minimize_window()

print(driver.title)  #OrangeHRM
print(driver.current_url)  #https://opensorce-demo.orangehrmlive.com/
print(driver.page_source)
driver.quit()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Program Files\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://demo.nopcommerce.com/")

###########--------find_element() -- Returns single webelement
# 1)Locator maching with single webelement

# element = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
# element.send_keys("Apple Macbook 13-inch")

# 2) Locator maching with multiple webelements
# element = driver.find_element(By.XPATH, "//div[@class='footer']//a")
# print(element.text) #prints first link from the footer "Sitemap"

# 3)Element not avalible then throw NoSuchElementException
# login_element = driver.find_element(By.LINK_TEXT, "Log")
# login_element.click()


###### find_elements()  - Returns multiple webelements

# 1)Locator maching with single webelemet
# elements = driver.find_elements(By.XPATH, "//input[@id='small-searchterms']")
# print(len(elements))  # 1
# elements[0].send_keys("Apple Macbook 13-inch")

# 2) Locator maching with multiple webelemets
# elements = driver.find_elements(By.XPATH, "//div[@class='footer']//a")
# print(len(elements))  # 23
# print(elements[0].text)  # 1  Sitemap
# for ele in elements:
#     print(ele.text)

# 3)Element not avalible - zero
elements = driver.find_elements(By.LINK_TEXT, "Log")
print("elements returned:", len(elements))

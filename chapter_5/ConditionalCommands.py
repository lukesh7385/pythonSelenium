from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Program Files\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.minimize_window()

# is_displayed()   is_enabled()

searchbox = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")

print("Display status:", searchbox.is_displayed())  # True
print("Enabled status:", searchbox.is_enabled())  # True

# is_selected() - for redio buttons check boxs
driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()

rd_male = driver.find_element(By.XPATH, "//input[@id='gender-male']")
rd_female = driver.find_element(By.XPATH, "//input[@id='gender-female']")

print("default radio button status.....")
print(rd_male.is_selected())  # False
print(rd_female.is_selected())  # False

rd_male.click()
print("after selecting male redio button.....")
print(rd_male.is_selected())  # True
print(rd_female.is_selected())  # false

rd_female.click()
print("after selecting female redio button.....")
print(rd_male.is_selected())  # false
print(rd_female.is_selected())  # True

driver.quit()

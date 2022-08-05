import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Program Files\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

# #  1) scroll down page by pixel
# driver.execute_script("window.scrollBy(0, 3000)", "")
# value = driver.execute_script("return window.pageYOffset;")
# print("Number of pixel move:", value)  # 3000

# #  2) scroll down page till the element is visible
# flag = driver.find_element(By.XPATH, "//img[@alt='Flag of India']")
# driver.execute_script("arguments[0].scrollIntoView();", flag)
# value = driver.execute_script("return window.pageYOffset;")
# print("Number of pixels moved:", value) # 4946

#  3) scroll down page till end
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:", value)  # 6000

time.sleep(5)
# scroll up to starting position
driver.execute_script("window.scrollBy(0, -document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:", value)  # 0

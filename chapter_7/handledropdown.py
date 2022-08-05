from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service("C:\Program Files\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()

# drpcountry = driver.find_element(By.XPATH, "//select[@id='input-country']")
drpcountry = Select(driver.find_element(By.XPATH, "//select[@id='input-country']"))

# select option for the dropdown
drpcountry.select_by_visible_text("India")  # we commonly used this option
# drpcountry.select_by_value("10")  # Argentina
# drpcountry.select_by_index(13)  # index

# capture all the options and print them
allOptions = drpcountry.options
print("Total number of options:", len(allOptions))

# for opt in allOptions:
#     print(opt.text)

# select options from dropdown without using built-in method
# for opt in allOptions:
#     if opt.text == "India":
#         opt.click()
#         break

allOptions = driver.find_elements(By.XPATH, '//*[@id="input-country"]/option')
print(len(allOptions)) # 242


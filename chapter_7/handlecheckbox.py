from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
serv_obj = Service("C:\Program Files\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

# 1) select specific checkbox
# driver.find_element(By.XPATH, "//input[@id='monday']").click()

# 2) select all the checkboxes
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkboxes))  # 7

# 1) Approach_1
# for i in range(len(checkboxes)):
#     checkboxes[i].click()

# 2) approach_2
for checkbox in checkboxes:
    checkbox.click()


# 3) select multiple checkboxes by choice
# for checkbox in checkboxes:
#     weekname = checkbox.get_attribute('id')
#     if weekname == 'monday' or weekname == 'sunday':
#         checkbox.click()

# 4) select lsat two checkboxes (formula :- 7-2=5) week=7, element you want to select = 2, starting element = 5
#  range(5,7) -->6,7
# formula totalnumberofelement-2=starting index
# for i in range(len(checkboxes)-4, len(checkboxes)):
#     checkboxes[i].click()


# 5) select first two  checkboxes
# for i in range(len(checkboxes)):
#     if i < 2:
#         checkboxes[i].click()

time.sleep(5)
# clearing all check boxes(using approach 2)
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()

driver.quit()

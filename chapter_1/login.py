# This is for selenium 3
#
# from selenium import webdriver
#
# driver = webdriver.Chrome(executable_path="C:\Program Files\Drivers\chromedriver.exe")
# driver.get("https://opensource-demo.orangehrmlive.com/")
# driver.find_element_by_name("txtUsername").clear()
# driver.find_element_by_name("txtUsername").send_keys("Admin")
# driver.find_element_by_id("txtPassword").clear()
# driver.find_element_by_id("txtPassword").send_keys("admin123")
# driver.find_element_by_name("Submit").click()
# act_title = driver.title
# exp_title = "OrangeHRM"
#
# if act_title == exp_title:
#     print("Login Test Passed")
# else:
#     print("Login Test Failed")
#
# driver.close()
# ------------------------------------------------------------------------------------------------
## This is for selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Program Files\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
# driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
driver.find_element(By.NAME, "txtUsername").clear()
driver.find_element(By.NAME, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").clear()
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()
act_title = driver.title
exp_title = "OrangeHRM"
if act_title == exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")

driver.close()

# ----------------------------------------------------------------------------------
# from selenium import webdriver
#
# # driver = webdriver.Chrome(executable_path="C:\Program Files\Drivers\chromedriver.exe")
# driver = webdriver.Chrome()
#
# driver.get("https://opensource-demo.orangehrmlive.com/")
# driver.find_element_by_name("txtUsername").clear()
# driver.find_element_by_name("txtUsername").send_keys("Admin")
# driver.find_element_by_id("txtPassword").clear()
# driver.find_element_by_id("txtPassword").send_keys("admin123")
# driver.find_element_by_name("Submit").click()
# act_title = driver.title
# exp_title = "OrangeHRM"
#
# if act_title == exp_title:
#     print("Login Test Passed")
# else:
#     print("Login Test Failed")
#
# driver.close()

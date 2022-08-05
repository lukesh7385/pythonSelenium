import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Program Files\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

windowid = driver.current_window_handle
print(windowid)  # CDwindow-3928FAB10DA9AFB46D3F186BF2D16713
#  CDwindow-23B2780F06830CCE2E1F181C08C1F7B8

driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
windowIDs = driver.window_handles

# 1)Approach
# parentwindowid = windowIDs[0]  # CDwindow-C7B062FBEF951D26B09944A47588BE1A
# childwindowid = windowIDs[1]  # CDwindow-D33414059B94CEC140F243672C219A2C
# # print(parentwindowid, childwindowid)
#
# driver.switch_to.window(childwindowid)
# print("titale of the child window:", driver.title)  #  OrangeHRM HR Software | Free & Open Source HR Software | HRMS | HRIS
#
# driver.switch_to.window(parentwindowid)
# print("titale of the parent window:", driver.title)  #  OrangeHRM
#
# driver.close()

# Approach 2
# for winid in windowIDs:
#     driver.switch_to.window(winid)
#     print(driver.title)

# time.sleep()
#
for winid in windowIDs:
    driver.switch_to.window(winid)
    if driver.title == "OrangeHRM HR Software | Free & Open Source HR Software | HRMS | HRIS":
        driver.close()

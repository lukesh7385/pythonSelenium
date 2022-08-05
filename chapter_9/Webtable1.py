from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Program Files\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#  count number of rows & columns
noOFrows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr"))
noOFcolumns = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr[1]/th"))
print(noOFrows)  # 7
print(noOFcolumns)  # 4

# ------------------------------------------------------------------------------------------

#  read specific row & Column data  - Master In Selenium
data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[5]/td[1]").text
print(data)  # Master In Selenium

# ----------------------------------------------------------------------------------------------
# read all the rows and column data
# print("All rows and columns data ----------------")
#
# for r in range(2, noOFrows + 1):
#     for c in range(1, noOFcolumns):
#         data = driver.find_element(By.XPATH,
#                                    "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[" + str(c) + "]").text
#         print(data, end='    ')
#     print()
# ----------------------------------------------------------------------------------------------------------
# Read data base on conditions(list books name whose auther is mukesh)
for r in range(2, noOFrows+1):
    authorName = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if authorName == "Mukesh":
        bookName = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]").text
        price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[4]").text
        print(bookName, "   ", authorName, "    ", price)

driver.close()

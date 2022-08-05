import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Program Files\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

driver.find_element(By.NAME, "txtUsername").clear()
driver.find_element(By.NAME, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").clear()
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()
time.sleep(3)

# Admin-->user management-->user
driver.find_element(By.XPATH, "//*[@id='menu_admin_viewAdminModule']/b").click()
driver.find_element(By.XPATH, "//*[@id='menu_admin_UserManagement']").click()
driver.find_element(By.XPATH, "//*[@id='menu_admin_viewSystemUsers']").click()

rows = len(driver.find_elements(By.XPATH, "//table[@id='resultTable']/tbody/tr"))
print("Total number of row in table: ", rows)

# count = 0
for r in range(1, rows + 1):
    username = driver.find_element(By.XPATH, "//table[@id='resultTable']/tbody/tr[" + str(r) + "]/td[2]").text
    userrole = driver.find_element(By.XPATH, "//table[@id='resultTable']/tbody/tr[" + str(r) + "]/td[3]").text
    status = driver.find_element(By.XPATH, "//table[@id='resultTable']/tbody/tr[" + str(r) + "]/td[5]").text
    if userrole == 'ESS':
        print(username, " ", userrole)
        if status == "Enabled":
            count = count + 1

print("Total number of user:", rows)
print("Number of enabled user:", count)
print("Number of disabled users:", (rows - count))

driver.close()
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from chapter_14 import XLUtils

serv_obj = Service("C:\Program Files\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-sbi"
           "-bsb001.html")
driver.maximize_window()

file ="C:\\Users\\lukesh\\PycharmProjects\\PythonTraining\\chapter_14\\caldata.xlsx"
rows = XLUtils.getRowCount(file, "Sheet1")
for r in range(2, rows + 1):
    pric = XLUtils.readData(file, "Sheet1", r, 1)
    rateofinterest = XLUtils.readData(file, "Sheet1", r, 2)
    pric1 = XLUtils.readData(file, "Sheet1", r, 3)
    pric2 = XLUtils.readData(file, "Sheet1", r, 4)
    fre = XLUtils.readData(file, "Sheet1", r, 5)
    exp_mvalue = XLUtils.readData(file, "Sheet1", r, 6)
    # passing data to the application

    driver.find_element(By.XPATH, "//input[@id='principal']").send_keys(pric)
    driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(rateofinterest)
    driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(pric1)
    perioddrp = Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
    perioddrp.select_by_visible_text(pric2)
    frequencydrp = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
    frequencydrp.select_by_visible_text(fre)
    driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[1]/img").click()  # calculate button
    act_mavalue = driver.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text

    # Validation

    if float(exp_mvalue) == float(act_mavalue):
        print("test passed")
        XLUtils.writeData(file, "Sheet1", r, 8, "Passed")
        XLUtils.fillGreenColor(file, "Sheet1", r, 8)
    else:
        print("test failed")
        XLUtils.writeData(file, "Sheet1", r, 8, "Failed")
        XLUtils.fillRedColor(file, "Sheet1", r, 8)
    driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[2]/img").click()
    time.sleep(2)

driver.close()




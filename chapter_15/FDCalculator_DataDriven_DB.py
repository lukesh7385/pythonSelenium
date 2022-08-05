import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import psycopg2

serv_obj = Service("C:\Program Files\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-sbi"
           "-bsb001.html")
driver.maximize_window()

try:
    con = psycopg2.connect(host="localhost", port="5050", user="postgres", password="system", database="empinfo")
    curs = con.cursor()  # create cursor
    curs.execute("select * from caldata")

    for row in curs:
        # reading data from database
        pric = row[0]
        rateofinterest = row[1]
        pric1 = row[2]
        pric2 = row[3]
        fre = row[4]
        exp_mvalue = row[5]

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

        else:
            print("test failed")
            driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[2]/img").click()
            time.sleep(2)
    con.close()
except:
    print("Connection unsuccessful....")
driver.close()
print("finished......")


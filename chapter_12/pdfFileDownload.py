from selenium import webdriver
from selenium.webdriver.common.by import By
import os

location = os.getcwd()


def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:\Program Files\Drivers\chromedriver.exe")
    #  download file in desired location
    preferences = {"download.default_directory": location, "plugins.always_open_df_externally": True}

    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preferences)
    driver = webdriver.Chrome(service=serv_obj, options=ops)
    return driver


def edge_setup():
    from selenium.webdriver.edge.service import Service
    serv_obj = Service("C:\Program Files\Drivers\msedgedriver.exe")
    #  download file in desired location
    preferences = {"download.default_directory": location, "plugins.always_open_df_externally": True}  # Have open bug
    ops = webdriver.EdgeOptions()
    ops.add_experimental_option("prefs", preferences)
    driver = webdriver.Edge(service=serv_obj, options=ops)
    return driver


def firefox_setup():
    from selenium.webdriver.firefox.service import Service
    serv_obj = Service("C:\Program Files\Drivers\geckodriver.exe")
    # settings
    ops = webdriver.FirefoxOptions()
    ops.set_preference("browser.helpApps.neverAsk.saveToDisk", "application/pdf")
    ops.set_preference("browser.download.manager.showWhenStarting", False)
    ops.set_preference("browser.download.folderList", 2)  # 0--desktop 1-download folder 2-desired location
    ops.set_preference("browser.download.dir", location)
    ops.set_preference("pdfjs.disabled", True)
    driver = webdriver.Firefox(service=serv_obj, options=ops)
    return driver


# Automation code
# driver = chrome_setup()
# driver = edge_setup()
driver = firefox_setup()

driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
driver.maximize_window()
driver.find_element(By.XPATH, "//tbody/tr[1]/td[5]/a[1]").click()


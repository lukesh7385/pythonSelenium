from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Program Files\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://money.rediff.com/gainers")
driver.maximize_window()

# self
# text_msg = driver.find_element(By.XPATH, "//a[contains(text(),'NDA Securities')]/self::a").text
# print(text_msg) #NDA Securities

# parent
# text_msg = driver.find_element(By.XPATH, "//a[contains(text(),'NDA Securities')]/parent::td").text
# print(text_msg) #NDA Securities

# child
# childs = driver.find_elements(By.XPATH, "//a[contains(text(),'NDA Securities')]/ancestor::tr/child::td")
# print(len(childs))  #5
# driver.close()

# Ancestor
# text_msg = driver.find_element(By.XPATH, "//a[contains(text(),'NDA Securities')]/ancestor::tr").text
# print(text_msg)  #NDA Securities X 10.01 10.65 + 6.39
# driver.close()

# Decendent
# descendants = driver.find_elements(By.XPATH, "//a[contains(text(),'NDA Securities')]/ancestor::tr/descendant::*")
# print("number of descendant Nodes:", len(descendants)) #7
# driver.close()

# following
# followings = driver.find_elements(By.XPATH, "//a[contains(text(),'NDA Securities')]/ancestor::tr/following::*")
# print("number of descendant Nodes:", len(followings)) #13375
# driver.close()

# following-sibling
# followingsiblings = driver.find_elements(By.XPATH, "//a[contains(text(),'NDA "
#                                                    "Securities')]/ancestor::tr/following-sibling::*")
# print("number of descendant Nodes:", len(followingsiblings)) #1652
# driver.close()

# Preceding
# precedings = driver.find_elements(By.XPATH, "//a[contains(text(),'NDA Securities')]/ancestor::tr/preceding::*")
# print(len(precedings)) #784
# driver.close()

# preceiding-sibling
precedingiblings = driver.find_elements(By.XPATH,
                                        "//a[contains(text(),'NDA Securities')]/ancestor::tr/preceding-sibling::tr")
print(len(precedingiblings))
driver.close()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=service)
 

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_hame = driver.find_element(By.NAME,"fName")
first_hame.send_keys("Angela")
last_name = driver.find_element(By.NAME,"lName")
last_name.send_keys("Yu")
email = driver.find_element(By.NAME,"email")
email.send_keys("dericcutie@gmail.com")

submit = driver.find_element(By.CSS_SELECTOR,"form button")
submit.click()


# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article_count = driver.find_element(By.CSS_SELECTOR,"#articlecount a")
# print(article_count.text)


# all_portals = driver.find_element(By.LINK_TEXT,"ALL portals")

# search = driver.find_element(By.NAME,"search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)
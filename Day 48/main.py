from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
 
service = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=service)
 
driver.get("https://www.python.org/")
event_times = driver.find_element(By.CSS_SELECTOR,".event-widget time")
event_names = driver.find_element(By.CSS_SELECTOR,".event-widget li a")
events = {}


for time in event_times:
    print(time.text)


# driver.get("https://www.amazon.com/fire-tv-stick-4k-max-with-alexa-voice-remote/dp/B09BS25XWH?th=1")
# price = driver.find_element(By.ID,"priceblock_ourprice")
# print(price.text)
# driver.quit()

# driver.get("https://www.python.org/")
# price = driver.find_element(By.ID,"priceblock-ourprice")
# print(price.text)

# search_bar = driver.find_element(By.NAME,"placeholder")
# logo = driver.find_element(By.CLASS_NAME,"python-logo")

# documentation_link = driver.find_element(By.CSS_SELECTOR(".documentation-widget a"))
# print(documentation_link.text)

# driver.close()
# driver.quit()
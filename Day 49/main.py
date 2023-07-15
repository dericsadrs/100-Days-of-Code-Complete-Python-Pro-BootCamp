from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime
import time
from selenium.common import StaleElementReferenceException, NoSuchElementException
 
 
def main():
 
    chrome_driver_path ="C:\Development\chromedriver.exe"
    service = Service(chrome_driver_path)
 
    cookie_clicker = webdriver.Chrome(service=service)
    cookie_clicker.get("https://orteil.dashnet.org/experiments/cookie/")
 
    cookie = cookie_clicker.find_element(By.ID, "cookie")
    ids = ["buyCursor", "buyGrandma", "buyFactory", "buyMine", "buyShipment", "buyAlchemy lab", "buyPortal", "buyTime machine"][::-1]
    element_tag = []
    current_time = time.time()
    time_out = time.time() + 60 * 5
    is_still_clicking = True
    while time.time() < time_out:
 
        cookie.click()
        for id_ in ids:
            element_tag.append(cookie_clicker.find_element(By.ID, id_))
        if time.time() >= current_time + 5:
 
            for tag in element_tag:
                try:
                    element = tag.find_element(By.CSS_SELECTOR, "b")
                except StaleElementReferenceException:
                    time.sleep(5)
                else:
                    price = upgrade_price(element)
 
                if price != "":
                    my_money = money(cookie_clicker.find_element(By.ID, "money").text)
                    my_money = int(my_money)
                    if my_money >= price:
                        tag.click()
                        break
            current_time = time.time()
 
    cookie_per_sec = cookie_clicker.find_element(By.ID, "cps")
    print(cookie_per_sec.text)
    cookie_clicker.quit()
 
 
 
 
def upgrade_price(element):
    try:
        product_cost = element.text.split("-")[1].strip()
    except IndexError:
        return ""
        pass
    else:
        product_cost = money(product_cost)
 
    return int(product_cost)
 
 
def money(amount):
    if "," in amount:
        amount = "".join(amount.split(","))
    return amount
 
main()
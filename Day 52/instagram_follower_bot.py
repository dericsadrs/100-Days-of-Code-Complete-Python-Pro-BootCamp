from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time, os
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

SIMILAR_ACCOUNT="simga_men"


#drive path
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
class InstaFollower:
    
    #constructor which has the parameter of path and the self
    def __init__(self, path):
        load_dotenv()
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        

        # finds the html tags in the web
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")


        # get environment variables
        username.send_keys(os.getenv("USERNAME"))
        password.send_keys(os.getenv("PASSWORD"))

        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(2)
        followers = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(2)
        modal = self.driver.find_element(By.XPATH,'/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR,"li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()
    def start_instagram_bot(self):
        self.login()
        self.find_followers()
        self.follow()

        


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.start_instagram_bot()


import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import smtplib

load_dotenv()
SENDER_EMAIL = os.getenv("MY_EMAIL")
SENDER_PASS = os.getenv("MY_PASSWORD")

url = "https://www.amazon.com.tr/SanDisk-SDSSDA-240G-G26-SSD-Plus-240GB/dp/B07621PNWC/ref=sr_1_1?keywords=ssd%2B240" \
      "%2Bgb&qid=1658063784&sprefix=ssd%2B%2Cspecialty-aps%2C108&sr=8-1&th=1"
header = {
    "Accept-Language": "en-US,en;q=0.9,tr;q=0.8,fa;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 "
                  "Safari/537.36",
}

response = requests.get(url=url, headers=header)
response.raise_for_status()
bs = BeautifulSoup(response.text, "lxml")
price_tl = int(bs.select_one("span.a-price-whole").getText().split(",")[0])
price_kr = int(bs.select_one("span.a-price-fraction").getText())
price = price_tl + (price_kr / 100)
print(price)
product_title = bs.select_one("span.a-size-large").getText().strip()
print(product_title)


# Send email
target_price = 500
if price < target_price:
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=SENDER_EMAIL, password=SENDER_PASS)
    message = f"{product_title} is now {price}\n{url}"
    receiver_mail = "drccsadrs@gmail.com"
    connection.sendmail(
        from_addr=SENDER_EMAIL,
        to_addrs=receiver_mail,
        msg=f"Subject:Amazon Price Alert\n\n{message}"
    )
    connection.close()
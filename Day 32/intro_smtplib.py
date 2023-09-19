
#
# Created on Sun Jun 25 2023
# Created by Software Engineer Deric San Andres
#


import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
my_email = os.getenv("MY_EMAIL")
password = os.getenv("MY_PASSWORD")
address_sent_to = "123@gmail.com"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs= address_sent_to, msg="Testing my python birthday wisher")
    connection.close()

#
# Created on Sun Jun 25 2023
# Created by Software Engineer Deric San Andres
#

import pandas
import smtplib
import datetime as dt
import random

my_email = "darsanandres@gmail.com"
password = "axauohgljmhhqqck"
address_sent_to = "drccsadrs@gmail.com"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 6:
    print("Triggerd")
    quotes = pandas.read_csv("quotes.txt")
    all_quotes = quotes.values.tolist()

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        print("Triggerd2")
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=address_sent_to, msg= str(all_quotes[random.randint(1,100)]).strip("[]"))
        connection.close()
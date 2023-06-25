#
# Created on Sun Jun 25 2023
# Created by Software Engineer Deric San Andres
#

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_the_week = now.weekday()


date_of_birth = dt.datetime(year= 2000, month=9,day=9)

print(date_of_birth)


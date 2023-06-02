#
# Created on Fri Jun 02 2023
# Created by Software Engineer Deric San Andres
#


for number in range(1,100):
    if number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else: 
        print(number)
#
# Created on Wed May 31 2023
# Created by Software Engineer Deric San Andres
#

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
if len(two_digit_number) == 2:
    sum_of_two_digit_number = two_digit_number[0]+two_digit_number[1]
    print(two_digit_number[0]  + " + " +  two_digit_number[1] + " = " + sum_of_two_digit_number)
else:
    print("Error input requires only two digit numbers (eg. Type a two digit number: 23")

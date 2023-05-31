#
# Created on Wed May 31 2023
# Created by Software Engineer Deric San Andres
#

# 🚨 Don't change the code below 👇
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bmi = weight / (height ** 2)
print("BMI:", bmi)
print("Rounded BMI:", round(bmi))

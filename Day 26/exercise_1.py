#
# Created on Sun Jun 11 2023
# Created by Software Engineer Deric San Andres
#
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
result = {word: len(word) for word in sentence.split()}

print(result.items())


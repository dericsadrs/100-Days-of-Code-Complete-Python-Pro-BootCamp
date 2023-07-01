#
# Created on Sun Jun 11 2023
# Created by Software Engineer Deric San Andres
#

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆

weather_f = {day: (temperature*9/5) + 32 for (day, temperature) in weather_c.items()}

# Write your code 👇 below:

# print(weather_f)
#

student_dict = {
    "student" : ["Angela", "James", "Lily"],
    "score" : [56,76,98]
}

import pandas

student_data_frame = pandas.DataFrame(student_dict)

print(student_data_frame)

for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)
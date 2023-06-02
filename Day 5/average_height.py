#
# Created on Fri Jun 02 2023
# Created by Software Engineer Deric San Andres
#

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
sum_of_student_heights = 0

for height_of_student in student_heights:
    sum_of_student_heights += height_of_student

average_student_heights =  round(sum_of_student_heights/(n + 1))

print(f"Sum of student heights: {sum_of_student_heights}")
print(f"Average student height: {average_student_heights}")

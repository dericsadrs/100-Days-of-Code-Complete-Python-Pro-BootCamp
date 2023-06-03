#
# Created on Sat Jun 03 2023
# Created by Software Engineer Deric San Andres
#
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for students in student_scores:
    if student_scores[students] >= 91:
        student_grades[students] = "Outstanding"
    elif student_scores[students] >= 81:
        student_grades[students] = "Exceeds Expectations"
    elif student_scores[students] >= 71:
        student_grades[students] = "Acceptable"
    else:
        student_grades[students] = "Fail"
    

# 🚨 Don't change the code below 👇
print(student_grades)
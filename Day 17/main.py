#
# Created on Tue Jun 06 2023
# Created by Software Engineer Deric San Andres
#

# class User:
#     def __init__(self, user_id,username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0
#     def follow(self,user):
#         user.followers += 1
#         self.following += 1
#
# user_1 = User("801", "Deric")
# user_2 = User("802", "Erika")
#
# user_1.follow(user_2)
#
# print(user_1.followers)

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print(f"You've completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")
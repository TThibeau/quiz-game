from question_model import Question
from data import question_data
import os

from quiz_brain import QuizBrain
os.system('cls || clear')

question_bank =[]
for question in question_data[0]["results"]:
    question_bank.append(Question(question['question'],question['correct_answer']))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():   
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your score is: {quiz.score}/{quiz.question_number}")
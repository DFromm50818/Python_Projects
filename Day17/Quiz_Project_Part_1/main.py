from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question_answer in question_data:
    question = question_answer["question"]
    answer = question_answer["correct_answer"]
    new_question = Question(question, answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the Quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

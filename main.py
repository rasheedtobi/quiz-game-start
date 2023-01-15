from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for quest in question_data:
    new_q = Question(quest["text"], quest["answer"])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)
while quiz.more_question():
    quiz.next_question()

# TruFalse
quiz.final_score()
# print(type(question_bank))

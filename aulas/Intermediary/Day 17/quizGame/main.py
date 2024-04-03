import data
from question_model import Question
question_bank = []

for element in data.question_data:
    question = element["text"]
    answer = element["answer"]
    question_bank.append(Question(question, answer))

print(question_bank)

student_scores = {"Gabriel": 89, "João": 92, "Maria": 23, "Evellyn": 65}
student_score_comment = {}

for nome in student_scores:
    if (student_scores[nome] <= 70):
        student_score_comment[nome] = "Fail"
    elif (student_scores[nome] > 70 and student_scores[nome] <= 80):
        student_score_comment[nome] = "Acceptable"
    elif (student_scores[nome] > 81 and student_scores[nome] <= 90):
        student_score_comment[nome] = "Exceeds Expectation"
    else:
        student_score_comment[nome] = "Outstanding"

print(student_score_comment)

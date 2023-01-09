student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

print("The highest score in the class is: ", max(student_scores))
print("The lowest score in the class is: ", min(student_scores))

# Output:
# Input a list of student scores 78 65 89 86 55 91 64 89
# [78, 65, 89, 86, 55, 91, 64, 89]
# The highest score in the class is:  91
# The lowest score in the class is:  55

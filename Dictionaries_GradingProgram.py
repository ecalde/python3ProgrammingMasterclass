# You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.
# Write a program that converts their scores to grades. By the end of the program, you shuold have a new dictionary called student_grades
# It should contain student names for keys and their grades for values.
# This is the scoring criteria:

#    Scores 91 - 100: Grade = "Outstanding"

#    Scores 81 - 90: Grade = "Exceeds Expectations"

#    Scores 71 - 80: Grade = "Acceptable"

#    Scores 70 or lower: Grade = "Fail"

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

sum = 0
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80 and score < 91:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70 and score < 81:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)
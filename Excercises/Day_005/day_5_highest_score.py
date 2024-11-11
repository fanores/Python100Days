#########################################
# Python Loops - Highest Score Example
#########################################

student_scores = [150, 142, 185, 120, 171, 46, 29, 30]

# Python function to sum list
print("Python function, SUM from a list: ")
total_student_scores = sum(student_scores)
print(total_student_scores)

# Manual sum of the score
print("Manual SUM of items in a list: ")
manual_total_student_scores = 0
for score in student_scores:
    manual_total_student_scores += score
print(manual_total_student_scores)

# Python function to find highest item in the list
print("Python function, MAX from a list: ")
print(max(student_scores))

# Manual MAX item from the score list
print("Manual MAX from items in a list: ")
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)

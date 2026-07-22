#student_scores_1 = [150, -142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
student_scores = [8 ,-33,-45,65, 89, 86, 55 ,91, 64, 89]
print(range(1, 10))
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(f"max score=+ {max_score}")

sum = 0
for score in student_scores:
    sum += score

print(f"sum={sum}")

min_score = 0
for score in student_scores:
    if score < min_score:
        min_score = score

print(f"min score={min_score}")
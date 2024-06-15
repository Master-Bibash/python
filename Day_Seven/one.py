# Read student data from input file
with open("D:\python\Day_Seven\input.txt", 'r') as file:
    lines = file.readlines()

student_scores = {}
for line in lines:
    data = line.strip().split()
    name = data[0]
    scores = []
    for score in data[1:]:
        scores.append(int(score))
    total_score = sum(scores)
    num_scores = len(scores)
    avg_score = total_score / num_scores
    student_scores[name] = avg_score

# Write student names and average scores to output file
with open('django_course/training_plan/day9/output.txt', 'w') as file:
    for name, avg_score in student_scores.items():
        file.write(f"{name} {avg_score:.2f}\n")

# Find student with highest average score
highest_avg_score = 0
top_student = ""
for name, avg_score in student_scores.items():
    if avg_score > highest_avg_score:
        highest_avg_score = avg_score
        top_student = name

# Print student with highest average score
print(f"Student with the highest average score: {top_student}")

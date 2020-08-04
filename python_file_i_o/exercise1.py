quizzes = [
    {"name": "Guillermo", "quiz1": 80, "quiz2": 85, "quiz3": 82},
    {"name": "Jamie", "quiz1": 78, "quiz2": 72, "quiz3": 80},
    {"name": "Otto", "quiz1": 92, "quiz2": 89, "quiz3": 96},
    {"name": "Christina", "quiz1": 91, "quiz2": 85, "quiz3": 94},
    {"name": "Ceasar", "quiz1": 62, "quiz2": 65, "quiz3": 73},
    {"name": "Barbara", "quiz1": 78, "quiz2": 68, "quiz3": 78},
    {"name": "Rosan", "quiz1": 84, "quiz2": 85, "quiz3": 81},
    {"name": "Marco", "quiz1": 79, "quiz2": 72, "quiz3": 87},
]
quizzes_names = ["quiz1", "quiz2", "quiz3"]
for student in quizzes:
    new_file = open(f'{student["name"]}_final_report.txt', "w")
    sum = 0
    for i in range(3):
        new_file.write(quizzes_names[i].capitalize() + ": " + str(student[quizzes_names[i]]) + "\n")
        sum += student[quizzes_names[i]]
    new_file.write(f'Average: {sum / 3}')

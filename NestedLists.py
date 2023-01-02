"""
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s)
of any student(s) having the second lowest grade.Note: If there are multiple students with the second lowest grade,
order their names alphabetically and print each name on a new line.
Example:
There are 5 students in this class whose names and grades are assembled to build the following list:
python_students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
The lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry,
so we order their names alphabetically and print each name on a new line.
"""

if __name__ == '__main__':
    students_with_second_lowest_score = []
    students_with_score = {}
    for _ in range(int(input("Enter student number: "))):
        name = input('Enter student name: ')
        score = float(input('Enter student score as float: '))
        students_with_score[name] = score
    filter_out_identical_scores = set(students_with_score.values())

    sorted_scores = sorted(filter_out_identical_scores)
    second_lowest_score = sorted_scores[1]

    for key, value in students_with_score.items():
        if value == second_lowest_score:
            students_with_second_lowest_score.append(key)

    students_with_second_lowest_score = sorted(students_with_second_lowest_score)

    for name in students_with_second_lowest_score:
        print(name)


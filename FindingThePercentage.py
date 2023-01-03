"""
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
Print the average of the marks array for the student name provided, showing 2 places after the decimal.
Example of key/value pairs:
'John Doe': [20, 30, 40] --> 30 average
'Jane Doe': [30, 50, 70] --> 50 average
query_name = input(student_name) --> Jane Doe
Ouput: 50.00
"""
if __name__ == '__main__':
    student_count = int(input('Enter how many students will be entered: '))
    student_average_scores = {}
    student_scores = {}
    for _ in range(student_count):
        name, *line = input('Enter student name and scores: (ex: John 10 20 30): ').split()
        scores = list(map(float, line))
        student_scores[name] = scores
    query_name = input('Enter student name to get average score: ')

    for key, value in student_scores.items():
        if key == query_name:
            average_score = float(sum(value) / len(value))
            answer = f"{average_score:.2f}"
            print(answer)
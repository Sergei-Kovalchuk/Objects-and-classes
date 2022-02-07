student_list = [
        { "name": "Ruoy", "surname": "Eman", "gender": "M", "course": "Python", "grade": [10, 10, 10, 9, 10, 10, 10, 10, 10, 10]},
        { "name": 'Bob', "surname": "Singer", "gender": "M", "course": "Python", "grade": [10, 5, 7, 9, 10, 10, 4, 9, 8, 6]}
]
def get_avg_hw_grade(students, course = 'Python'):
    sum_hw = 0
    for student in students:
        if student['course'] == course:    
            sum_hw += sum(student['grade']) / len(student['grade'])
    return round(sum_hw / len(students), 2)      
print(f'Средняя оценка всех студентов: {get_avg_hw_grade(student_list)}')


lectures_list = [
    { "name": "Some", "surname": "Buddy", "course": "Python", "grade": [10, 10, 10, 9, 10, 10, 10, 10, 10, 10]},
    { "name": "Margo", "surname": "Buddy", "course": "Python", "grade": [10, 10, 4, 6, 10, 8, 7, 7, 10, 9]}
]    
def get_avg_hw_grade(lecturer, course = 'Python'):
    sum_lc = 0
    for lector in lecturer:
        if lector['course'] == course:    
            sum_lc += sum(lector['grade']) / len(lector['grade'])
    return round(sum_lc / len(lecturer), 2)      
print(f'Средняя оценка всех лекторов: {get_avg_hw_grade(lectures_list)}')
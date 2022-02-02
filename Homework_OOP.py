class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.sum_hw = 0
    def rate_lc(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:

            if course in lector.grade_book:
                lector.grade_book[course] += [grade]
            else:
                lector.grade_book[course] = [grade]
        else:
            return 'Ошибка!'
    def _get_avg_hw_grade(self):
        self.sum_hw += sum(self.grades['Python']) / len(self.grades['Python'])
        return self.sum_hw
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._get_avg_hw_grade()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res
    def __delattr__(self, other):
        self._get_avg_hw_grade()
        return self.sum_hw < other.sum_hw
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
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.name = name
        self.surname = surname
        self.courses_attached = [] 

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        name_reviewer = f'Имя: {self.name}\nФамилия: {self.surname}'
        return name_reviewer
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grade_book = {} 
        self.sum_gd = 0
    def _get_avg_lc_grade(self):
        self.sum_gd += sum(self.grade_book['Python']) / len(self.grade_book['Python'])
        return self.sum_gd   
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._get_avg_lc_grade()}'
        return res
    def __delattr__(self, other):
        self._get_avg_lc_grade()
        return self.sum_gd > other.sum_gd 
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
    print (f'Средняя оценка всех лекторов: {get_avg_hw_grade(lectures_list)}')
some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в программирование']
other_student = Student('Bob', 'Singer', 'М') 
other_student.courses_in_progress += ['Python','Git']
other_student.finished_courses += ['Введение в программирование']
 
some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']
other_reviewer = Reviewer('Margo', 'Buddy')
other_reviewer.courses_attached += ['Python']

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']
other_lecturer = Lecturer('Elli', 'Bush')
other_lecturer.courses_attached += ['Python']
 
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)

some_reviewer.rate_hw(other_student, 'Python', 10)
some_reviewer.rate_hw(other_student, 'Python', 5)
some_reviewer.rate_hw(other_student, 'Python', 7)
some_reviewer.rate_hw(other_student, 'Python', 9)
some_reviewer.rate_hw(other_student, 'Python', 10)
some_reviewer.rate_hw(other_student, 'Python', 10)
some_reviewer.rate_hw(other_student, 'Python', 4)
some_reviewer.rate_hw(other_student, 'Python', 9)
some_reviewer.rate_hw(other_student, 'Python', 8)
some_reviewer.rate_hw(other_student, 'Python', 6)

some_student.rate_lc(some_lecturer, 'Python', 10)
some_student.rate_lc(some_lecturer, 'Python', 10)
some_student.rate_lc(some_lecturer, 'Python', 10)
some_student.rate_lc(some_lecturer, 'Python', 9)
some_student.rate_lc(some_lecturer, 'Python', 10)
some_student.rate_lc(some_lecturer, 'Python', 10)
some_student.rate_lc(some_lecturer, 'Python', 10)
some_student.rate_lc(some_lecturer, 'Python', 10)
some_student.rate_lc(some_lecturer, 'Python', 10)
some_student.rate_lc(some_lecturer, 'Python', 10)

some_student.rate_lc(other_lecturer, 'Python', 10)
some_student.rate_lc(other_lecturer, 'Python', 10)
some_student.rate_lc(other_lecturer, 'Python', 4)
some_student.rate_lc(other_lecturer, 'Python', 6)
some_student.rate_lc(other_lecturer, 'Python', 10)
some_student.rate_lc(other_lecturer, 'Python', 8)
some_student.rate_lc(other_lecturer, 'Python', 7)
some_student.rate_lc(other_lecturer, 'Python', 7)
some_student.rate_lc(other_lecturer, 'Python', 10)
some_student.rate_lc(other_lecturer, 'Python', 9)
 
 
print(other_student)
print(other_lecturer)
print(other_reviewer)
print(some_reviewer)
print(some_lecturer)
print(some_student)
print(some_lecturer.__delattr__(other_lecturer))
print(some_student.__delattr__(other_student))
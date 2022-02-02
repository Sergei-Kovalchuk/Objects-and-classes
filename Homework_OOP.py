class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.sum_hw = 0
    def _get_avg_hw_grade(self):
        self.sum_hw += sum(self.grades['Python']) / len(self.grades['Python'])
        return self.sum_hw
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._get_avg_hw_grade()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res
    def __delattr__(self, other):
        self._get_avg_hw_grade()
        return self.sum_hw < other.sum_hw
    def rate_lc(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:

            if course in lector.grade_book:
                lector.grade_book[course] += [grade]
            else:
                lector.grade_book[course] = [grade]
        else:
            return 'Ошибка!'    
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
 
print(some_reviewer)
print(some_lecturer)
print(some_student)
print(some_lecturer.__delattr__(other_lecturer))
print(some_student.__delattr__(other_student))
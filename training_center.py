class Courses(object):
    """Было бы классно еще классно привязать сюда учителей и студентов, но у меня не получилось напрямую"""
    def __init__(self, name, teachers, students):
        self.name = name
        self.teachers = [teachers]
        self.students = [students]

    def set_name(self, name):
        self.name = name

    def set_teachers(self, teacher):
        self.students.append(teacher)

    def set_students(self, student):
        self.students.append(student)

    def show(self):
        return 'Предмет: {} | Препод: {} | Студенты: {}'. format(self.name, self.teachers, self.students)

    """Учителя и студенты с курсов не удаляются. Потому что раз попав на курс, ты не можешь с него сойти"""
    """И я что-то не уловил и просто сделал как в лекции"""


class People(object):
    """Т.к. и в учителе и в студенте есть имя и фамилия, то можно сделать этот класс, а потом унаследоваться от него"""
    def __init__(self, firstname, surname):
        self.firstname = firstname
        self.surname = surname

    def set_fname(self, firstname):
        self.firstname = firstname

    def set_sname(self, surname):
        self.surname = surname


class Teachers(People):
    def __init__(self, firstname, surname, lead_courses, students):
        super().__init__(firstname, surname)
        self.lead_courses = [lead_courses]
        self.students = [students]

    def set_students(self, student):
        self.students.append(student)

    def show(self):
        return 'Имя: {} | Фамилия: {} | Ведет курсы: {} | Студенты: {}'. format(self.firstname,
                                                                                self.surname,
                                                                                self.lead_courses,
                                                                                self.students)



class Students(People):
    def __init__(self, firstname, surname, courses, teachers):
        super().__init__(firstname, surname)
        self.courses = [courses]
        self.teachers = [teachers]

    def set_teachers(self, teacher):
        self.teachers.append(teacher)

    def show(self):
        return 'Имя: {} | Фамилия: {} | Ходит на курсы: {} | Учителя: {}'. format(self.firstname,
                                                                                  self.surname,
                                                                                  self.courses,
                                                                                  self.teachers)


"""Как не таскать с собой из класса в класс метод .show, а отнаследовать и где-то просто в него добалять инфу?"""

"""
teacher = Teachers('Катя', 'Иванова', 'Math', 'Пупкин')
student = Students('Вова', 'Вовин', 'Rus', 'Rusgenius')
courseRUS = Courses('Rus', 'Rusgenius', ['Пупкин', 'Вовин'])

teacher.set_students('Залупкин')
print(teacher.show(),
      student.show(),
      courseRUS.show(), sep='\n'
)
"""
class Courses(object):
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


class Teachers(object):
    def __init__(self, firstname, surname, lead_courses, students):
        self.firstname = firstname
        self.surname = surname
        self.lead_courses = [lead_courses]
        self.students = students


class Students(object):
    def __init__(self, firstname, surname, courses, teachers):
        self.firstname = firstname
        self.surname = surname
        self.courses = courses
        self.teachers = teachers

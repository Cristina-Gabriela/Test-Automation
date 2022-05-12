class Person:  # clasa parinte
    def __init__(self, name, surname, number):
        self.name = name
        self.surname = surname
        self.number = number
        self._height = 50  # protected field


class Student(Person):  # clasa copil
    UNDERGRADUATE = 0
    POSTGRADUATE = 1

    # UNDERGRADUATE, POSTGRADUATE = range(2)

    def __init__(self, student_type, *args, **kwargs):  # constructor
        self.student_type = student_type  # Proprietatea clasei de student
        self.cursuri = []  # initializat lista de cursuri
        super(Student, self).__init__(*args, **kwargs)
        self.note = {}

    def enroll(self, course):
        self.cursuri.append(course)
        self._height = 20

    def receive_grade(self, nota, materie):

        if materie in self.cursuri:
            self.note[materie] = nota

    def afiseaza_note(self):
        for course_name in self.note:
            print(course_name, self.note[course_name])


class StaffMember(Person):  # clasa copil
    PERMANENT, TEMPORARY = range(2)

    def __init__(self, employment_type, *args, **kwargs):
        self.employment_type = employment_type
        super(StaffMember, self).__init__(*args, **kwargs)


class Lecturer(StaffMember):  # clasa copilul copilului
    def __init__(self, *args, **kwargs):
        self.courses_taught = []
        super(Lecturer, self).__init__(*args, **kwargs)

    def assign_teaching(self, course):
        self.courses_taught.append(course)


jane: Student = Student(Student.POSTGRADUATE, "Jane", "Smith", "SMTJNX05455")

jane.enroll("math")
jane.receive_grade(10, "math")
jane.afiseaza_note()

print("Inainte de fizica")

jane.enroll("Fizica")
jane.receive_grade(2, "biofizica")
jane.afiseaza_note()
# bob = Lecturer(StaffMember.PERMANENT, "Bob", 'Jones', "256415")
# bob.assign_teaching(an_undergrad_course)


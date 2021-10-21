from enum import Enum


class Student:
    def __init__(self, name):
        self.name = name
        self.year = Year.Freshman
        self.courses = []

    def add_course(self, course):
        if course.not_full():
            course.update_enrollment(1)
            self.courses.append(course)
            self.update_year()
            return True
        return False

    def student_remove_course(self, course):  # to be used by
        while course in self.courses:  # remove all instances of the course if it was added multiple times
            self.courses.remove(course)
            course.update_enrollment(-1)
        self.update_year()

    def get_year(self):
        return self.year

    def get_name(self):
        return self.name

    def get_courses(self):
        return self.courses

    def set_name(self, name):
        self.name = name

    def update_year(self):
        if len(self.courses) <= 2:
            self.year = Year.Freshman
        elif len(self.courses) <= 4:
            self.year = Year.Sophomore
        elif len(self.courses) <= 6:
            self.year = Year.Junior
        elif len(self.courses) <= 8:
            self.year = Year.Senior
        else:
            self.year = Year.Graduate


class Professor:
    def __init__(self, name):
        self.name = name
        self.salary = 0
        self.courses = []

    def __eq__(self, other):
        return self.name == other.name

    def add_course_prof(self, course):
        self.courses.append(course)

    def prof_remove_course(self, course):
        while course in self.courses:
            self.courses.remove(course)

    def calculate_salary(self):
        self.salary = len(self.courses) * 10000

    def get_salary(self):
        return self.salary

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


class Course:
    def __init__(self, title, capacity, instructor_name):
        self.title = title
        self.capacity = capacity
        self.enrollment = 0
        self.instructor_name = instructor_name

    def __eq__(self, other):
        return self.title == other.title

    def update_enrollment(self, i):
        self.enrollment += i

    def not_full(self):
        return self.enrollment < self.capacity

    def get_capacity(self):
        return self.capacity

    def get_enrollment(self):
        return self.enrollment

    def get_title(self):
        return self.title

    def get_prof(self):
        return self.instructor_name


class School:
    def __init__(self):
        self.students = []
        self.courses = []
        self.professors = []

    def add_student(self, name):
        s = Student(name)
        self.students.append(s)
        return s

    def add_professor(self, name):
        p = Professor(name)
        self.professors.append(Professor(name))
        return p

    def register_course(self, student_name, course_name):
        found = False
        for s in self.students:
            if s.get_name() == student_name:
                student = s
                found = True
        if not found:
            student = self.add_student(student_name)
        for c in self.courses:
            if c.get_title() == course_name:
                student.add_course(c)

    def new_course(self, title, capacity, instructor_name):
        found = False
        for p in self.professors:
            if p.get_name == instructor_name:
                instructor = p
                found = True
        if not found:
            instructor = self.add_professor(instructor_name)
        new_course = Course(title, capacity, instructor_name)
        self.courses.append(new_course)
        self.professors[self.professors.index(instructor)].add_course_prof(new_course)

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            return True
        return False

    def remove_course(self, course):
        for student in self.students:
            student.student_remove_course(course)
        for professor in self.professors:
            professor.prof_remove_course(course)

    def remove_professor(self, professor):
        if professor in self.professors:
            self.professors.remove(professor)
            return True
        return False

    def get_students(self):
        return self.students

    def get_courses(self):
        return self.courses

    def get_professors(self):
        return self.professors

    # def register_for_course(self, course, student):
    #     if student in self.students:
    #         self.students[self.students.index(student)].add_course(course)


class Year(Enum):
    Freshman = 1
    Sophomore = 2
    Junior = 3
    Senior = 4
    Graduate = 5


def main():
    uvm = School()

    uvm.add_student("Kevin")
    uvm.add_student("Clayton")
    uvm.add_student("Zach")

    uvm.new_course("CS 205", 2, "Jason")

    uvm.register_course("Kevin", "CS 205")
    uvm.register_course("Clayton", "CS 205")
    # zach was too slow to register... what a bummer
    uvm.register_course("Zach", "CS 205")

    students = uvm.get_students()
    for s in students:
        print(s.get_courses)


main()

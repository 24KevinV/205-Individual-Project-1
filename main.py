from enum import Enum


class Student:
    def __init__(self, name):
        self.name = name
        self.year = Year.Freshman
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)
        if len(self.courses) <= 10:
            self.year = Year.Freshman
        elif len(self.courses) <= 20:
            self.year = Year.Sophomore
        elif len(self.courses) <= 30:
            self.year = Year.Junior
        elif len(self.courses) <= 40:
            self.year = Year.Senior
        else:
            self.year = Year.Graduate

    def get_year(self):
        return self.year

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


class Professor:
    def __init__(self):
        self.name = 'New Professor'
        self.salary = 0
        self.courses = []

    def add_courses(self, course):
        self.courses.append(course)

    def calculate_salary(self):
        self.salary = len(self.courses) * 10000

    def get_salary(self):
        return self.salary

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


class Course:
    def __init__(self, title, capacity, instructor):
        self.title = title
        self.capacity = capacity
        self.enrollment = 0
        self.instructor = instructor

    def __eq__(self, course):
        return self.title == course.title
        

class Year(Enum):
    Freshman = 1
    Sophomore = 2
    Junior = 3
    Senior = 4
    Graduate = 5

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


class Year(Enum):
    Freshman = 1
    Sophomore = 2
    Junior = 3
    Senior = 4
    Graduate = 5

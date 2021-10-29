from enum import Enum


class Student:
    def __init__(self, name):
        self.name = name
        self.year = Year.Freshman
        self.courses = []

    def __str__(self):
        course_string = "\n"
        if len(self.courses) == 0:
            course_string += "\tNot enrolled in any courses :("
        else:
            for c in self.courses:
                course_string += "\t" + str(c) + "\n"
        return self.name + ", " + str(self.year) + course_string

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

    def __str__(self):
        course_string = "\n"
        if len(self.courses) == 0:
            course_string += "\tNot teaching any courses :("
        else:
            for c in self.courses:
                course_string += "\t" + str(c) + "\n"
        return self.name + ", Salary: " + str(self.salary) + course_string

    def add_course_prof(self, course):
        self.courses.append(course)
        self.calculate_salary()

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

    def __str__(self):
        return self.title + ", Enrollment: " + str(self.enrollment) + "/"\
               + str(self.capacity) + " Professor: " + self.instructor_name

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
                if student.add_course(c):
                    return 0
                return 2
        return 1

    def get_students_in_course(self, course_name):
        found = False
        for c in self.courses:
            if c.get_title() == course_name:
                course = c
                found = True
        if not found:
            return None
        students = []
        for s in self.students:
            if course in s.get_courses():
                students.append(s)
        if len(students) == 0:
            students.append(None)
        return students

    def new_course_incorrect(self, title, capacity, instructor_name):
        found = False
        for p in self.professors:
            if p.get_name == instructor_name:  # sneaky bug doesn't crash but will never be true so adds new professor
                instructor = p
                found = True
        if not found:
            instructor = self.add_professor(instructor_name)
        new_course = Course(title, capacity, instructor_name)
        self.courses.append(new_course)
        self.professors[self.professors.index(instructor)].add_course_prof(new_course)

    def new_course(self, title, capacity, instructor_name):
        found = False
        for p in self.professors:
            if p.get_name() == instructor_name:
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

    def __str__(self):
        return self.name


def main():
    uvm = School()
    print("Students and Professors are created automatically")
    print("Courses need to be created before they can be registered for")
    stop = False
    while not stop:
        choice = input("Create Course (c), Print Info (p), Register for a Course (r), "
                       "Get list of students in a course (g), Quit (q): ")
        if choice == 'c':
            prof = input("Professor Name: ")
            title = input("Course Title: ")
            try:
                capacity = int(input("Max Enrollment (integer): "))
            except ValueError:
                print("Seriously? All you had to do was enter an int.")
                capacity = 10
            uvm.new_course(title, capacity, prof)
        elif choice == 'p':
            print("========== Students ==========")
            students = uvm.get_students()
            for s in students:
                print(s)

            print("========= Professors =========")
            professors = uvm.get_professors()
            for p in professors:
                print(p)

            print("========== Courses ===========")
            courses = uvm.get_courses()
            for c in courses:
                print(c)
        elif choice == 'r':
            title = input("Course Title: ")
            name = input("Student Name: ")
            rc = uvm.register_course(name, title)
            if rc == 1:
                print("Invalid Course Title")
            elif rc == 2:
                print("Course Full")
        elif choice == 'g':
            course_name = input("Course Title: ")
            student_list = uvm.get_students_in_course(course_name)
            if student_list is None:
                print(course_name + " Does Not Exist")
            elif None in student_list:
                print("No students in " + course_name)
            else:
                print("Students in " + course_name + ":")
                for s in student_list:
                    print(s.get_name() + ", " + str(s.get_year()))
            print('')
        elif choice == 'q':
            stop = True


if __name__ == '__main__':
    main()

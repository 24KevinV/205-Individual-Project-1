import unittest
import main


class TestSchool(unittest.TestCase):
    school = None

    @classmethod
    def setUpClass(cls):
        print("setUpClass()")
        cls.school = main.School()

        # create class variables to easily create things later
        cls.course_1 = "CS 205"
        cls.course_2 = "CS 211"
        cls.course_3 = "CS 275"
        cls.prof_1 = "Jason"
        cls.prof_2 = "Joe"
        cls.student_1 = "Kevin"
        cls.student_2 = "Clayton"
        cls.student_3 = "Zach"
        cls.student_4 = "Anthony"
        cls.student_5 = "Cole"
        cls.capacity_1 = 1
        cls.capacity_2 = 2
        cls.capacity_3 = 4

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass()")

    def setUp(self):
        print("setUp()")
        # make the courses, students, professors
        self.school.new_course(self.course_1, self.capacity_1, self.prof_1)
        self.school.new_course(self.course_2, self.capacity_2, self.prof_2)
        self.school.new_course(self.course_3, self.capacity_3, self.prof_1)
        self.school.register_course(self.student_1, self.course_1)
        self.school.register_course(self.student_1, self.course_2)
        self.school.register_course(self.student_4, self.course_2)
        # self.school.register_course(self.student_5, self.course_2)  # student 5 not in course 2 because it is full
        self.school.register_course(self.student_1, self.course_3)
        self.school.register_course(self.student_2, self.course_3)
        self.school.register_course(self.student_3, self.course_3)

    def tearDown(self):
        print("tearDown()")
        self.school.remove_all()

    # ------------------------------------------------------------------------------------------------------------------

    # noinspection DuplicatedCode
    def test_new_course_incorrect(self):
        # Makes a new course for prof 1 there should only be 2 professors since it should add the course to the current
        # prof_1 instead of making a new one
        self.school.new_course_incorrect("CS 222", 2, self.prof_1)
        # checks that the number of professors is still 2 as it should be
        self.assertEqual(len(self.school.get_professors()), 2)
        # check that the course was added to the list of courses maintained in school
        found = False
        for c in self.school.get_courses():
            if "CS 222" == c.get_title():
                found = True
        self.assertEqual(found, True)
        prof = None
        for p in self.school.get_professors():
            if self.prof_1 == p.get_name():
                prof = p
        self.assertIsNotNone(prof)  # find the professor
        # check that the course was added to the professor's list of courses
        found = False
        for c in prof.get_courses():
            if "CS 222" == c.get_title():
                found = True
        self.assertEqual(found, True)

    # ------------------------------------------------------------------------------------------------------------------

    # noinspection DuplicatedCode
    def test_new_course(self):
        # Makes a new course for prof 1 there should only be 2 professors since it should add the course to the current
        # prof_1 instead of making a new one
        self.school.new_course("CS 222", 2, self.prof_1)
        # checks that the number of professors is still 2 as it should be
        self.assertEqual(len(self.school.get_professors()), 2)
        # check that the course was added to the list of courses maintained in school
        found = False
        for c in self.school.get_courses():
            if "CS 222" == c.get_title():
                found = True
        self.assertEqual(found, True)
        prof = None
        for p in self.school.get_professors():
            if self.prof_1 == p.get_name():
                prof = p
        self.assertIsNotNone(prof)  # find the professor
        # check that the course was added to the professor's list of courses
        found = False
        for c in prof.get_courses():
            if "CS 222" == c.get_title():
                found = True
        self.assertEqual(found, True)

    # ------------------------------------------------------------------------------------------------------------------

    def test_register_course(self):
        # student 5 isn't in anything and shouldn't exist
        student_names = [s.get_name() for s in self.school.get_students()]
        self.assertNotIn(self.student_5, student_names)
        # adding student 5 to course 3, should return 0
        rc = self.school.register_course(self.student_5, self.course_3)
        self.assertEqual(rc, 0)
        # student 5 should exist now
        student_names = [s.get_name() for s in self.school.get_students()]
        self.assertIn(self.student_5, student_names)

        # adding student 1 to a course that doesn't exist should return 1
        rc = self.school.register_course(self.student_1, "CS 292")
        self.assertEqual(rc, 1)

        # trying to add student 5 to course 2 should return 2 because the course is full
        rc = self.school.register_course(self.student_5, self.course_2)
        self.assertEqual(rc, 2)

    # ------------------------------------------------------------------------------------------------------------------

    # noinspection DuplicatedCode
    def test_get_students_in_course(self):
        # checks that only the students who registered for course_3 are in it and that they are all in it
        students = self.school.get_students_in_course(self.course_3)
        self.assertEqual(len(students), 3)
        student_names = [students[i].get_name() for i in range(3)]
        self.assertIn(self.student_1, student_names)
        self.assertIn(self.student_2, student_names)
        self.assertIn(self.student_3, student_names)
        self.assertNotIn(self.student_4, student_names)

        self.school.register_course(self.student_5, self.course_3)
        # added a student and check again
        students = self.school.get_students_in_course(self.course_3)
        self.assertEqual(len(students), 4)
        student_names = [students[i].get_name() for i in range(4)]
        self.assertIn(self.student_1, student_names)
        self.assertIn(self.student_2, student_names)
        self.assertIn(self.student_3, student_names)
        self.assertIn(self.student_5, student_names)
        self.assertNotIn(self.student_4, student_names)

    # ------------------------------------------------------------------------------------------------------------------

    def test_get_year(self):
        # get the student 1 object from the school
        students = self.school.get_students()
        student_1 = None
        for s in students:
            if self.student_1 == s.get_name():
                student_1 = s
        # student should be in the school somewhere
        self.assertIsNotNone(student_1)
        # student 1 is in 3 courses and should be a sophomore
        self.assertEqual(student_1.get_year(), main.Year.Sophomore)

        # make and register for 2 more courses, student 1 should be a junior now
        self.school.new_course("CS 292", 1, "Lisa")
        self.school.new_course("CS 202", 1, "Joe")

        self.school.register_course(self.student_1, "CS 292")
        self.school.register_course(self.student_1, "CS 202")

        self.assertEqual(student_1.get_year(), main.Year.Junior)

    # ------------------------------------------------------------------------------------------------------------------

    def test_delete_student(self):
        student_1 = self.school.get_students()[0]
        courses = student_1.get_courses()
        # check the enrollments are what we think they should be
        self.assertEqual(courses[0].get_enrollment(), 1)
        self.assertEqual(courses[1].get_enrollment(), 2)
        self.assertEqual(courses[2].get_enrollment(), 3)
        # check that the student is in the courses
        self.assertIn(student_1, self.school.get_students_in_course(self.course_1))
        self.assertIn(student_1, self.school.get_students_in_course(self.course_2))
        self.assertIn(student_1, self.school.get_students_in_course(self.course_3))

        self.school.delete_student(student_1)

        # check that enrollment went down by one
        self.assertEqual(courses[0].get_enrollment(), 0)
        self.assertEqual(courses[1].get_enrollment(), 1)
        self.assertEqual(courses[2].get_enrollment(), 2)

        # check that the student is not in the courses anymore
        self.assertNotIn(student_1, self.school.get_students_in_course(self.course_1))
        self.assertNotIn(student_1, self.school.get_students_in_course(self.course_2))
        self.assertNotIn(student_1, self.school.get_students_in_course(self.course_3))

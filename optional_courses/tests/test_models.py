from django.test import TestCase

from . import create_initial_data


class ModelTests(TestCase):

    def setUp(self):
        create_initial_data(self)

    def test_specialization_str(self):
        self.assertEqual(str(self.specialization_1), "Economic cybernetics")

    def test_university_group_str(self):
        self.assertEqual(str(self.group_1), "IE-401")

    def test_field_str(self):
        self.assertEqual(str(self.field_2), "Math and logic")

    def test_course_str(self):
        self.assertEqual(str(self.course_2), "Combinatorial game theory")

    def test_student_with_custom_fields_str(self):
        self.assertEqual(self.student_1.group, self.group_1)
        self.assertEqual(self.student_1.courses.first(), self.course_1)
        self.assertEqual(str(self.student_1), "Maria Samkova (mariasamkova)")

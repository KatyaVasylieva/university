from django.test import TestCase

from optional_courses.models import Specialization, UniversityGroup,\
    Field, Course, Student


class ModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.specialization = Specialization.objects.create(
            name="Economic cybernetics",
            description="Economic systems, mathematical modeling"
        )

        cls.field = Field.objects.create(
            name="Math and logic"
        )

        cls.course = Course.objects.create(
            title="Combinatorial game theory"
        )

    def test_specialization_str(self):
        self.assertEqual(str(self.specialization), "Economic cybernetics")

    def test_university_group_str(self):
        student_group = UniversityGroup.objects.create(
            short_name="IE-401",
            specialization=self.specialization,
        )
        self.assertEqual(str(student_group), "IE-401")

    def test_field_str(self):
        self.assertEqual(str(self.field), "Math and logic")

    def test_course_str(self):
        self.assertEqual(str(self.course), "Combinatorial game theory")

    def test_student_with_custom_fields_str(self):
        student_group = UniversityGroup.objects.create(
            short_name="IE-401",
            specialization=self.specialization,
        )
        student = Student.objects.create(
            username="ivan1234",
            first_name="Ivan",
            last_name="Harbuz",
            group=student_group,
        )
        student.courses.set([self.course])
        self.assertEqual(student.group, student_group)
        self.assertEqual(student.courses.first(), self.course)
        self.assertEqual(str(student), "Ivan Harbuz (ivan1234)")

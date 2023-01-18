from django.test import TestCase

from optional_courses.forms import CourseCreateForm, CourseUpdateFieldsForm, StudentCreationForm
from optional_courses.models import Field, Course, Specialization, UniversityGroup


class FormTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.field_ds = Field.objects.create(
            name="Data science"
        )

        cls.field_m = Field.objects.create(
            name="Math and logic"
        )

        cls.field_cs = Field.objects.create(
            name="Computer sciense"
        )

        cls.field_e = Field.objects.create(
            name="Engineering"
        )

        cls.specialization_ec = Specialization.objects.create(
            name="Economic cybernetics",
            description="Economic systems, mathematical modeling"
        )

    def test_course_create_form(self):

        form_data = {
            "title": "Unsupervised learning",
            "fields": [self.field_ds, self.field_m],
        }

        form = CourseCreateForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["title"], form_data["title"])
        self.assertEqual(
            list(form.cleaned_data["fields"]),
            form_data["fields"]
        )

    def test_course_create_form_with_more_than_3_fields(self):

        form_data = {
            "title": "Unsupervised learning",
            "fields": [
                self.field_ds, self.field_m, self.field_cs, self.field_e
            ],
        }

        form = CourseCreateForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_course_update_fields_form(self):
        course = Course.objects.create(
            title="Unsupervised learning",
        )
        course.fields.set([self.field_ds])

        form_data = {
            "fields": [self.field_ds, self.field_m]
        }

        form = CourseUpdateFieldsForm(data=form_data)

        self.assertTrue(form.is_valid())
        case = form.save()
        self.assertEqual(form_data["fields"], list(case.fields.all()))

    def test_course_update_form_with_more_than_3_fields(self):

        course = Course.objects.create(
            title="Unsupervised learning",
        )
        course.fields.set([self.field_ds])

        form_data = {
            "fields": [
                self.field_ds, self.field_m, self.field_cs, self.field_e
            ]
        }

        form = CourseUpdateFieldsForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_student_create_form(self):

        group_ie1 = UniversityGroup.objects.create(
            short_name="IE-401",
            specialization=self.specialization_ec
        )

        form_data = {
            "username": "mariasamkova",
            "first_name": "Maria",
            "last_name": "Samkova",
            "group": group_ie1,
            "password1": "hellobeautiful",
            "password2": "hellobeautiful",
        }

        form = StudentCreationForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

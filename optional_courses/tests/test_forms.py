from django.contrib.auth import get_user_model
from django.test import TestCase

from optional_courses.forms import CourseCreateForm, CourseUpdateFieldsForm, StudentCreationForm
from optional_courses.models import Field, Course, Specialization, UniversityGroup


class FormTests(TestCase):

    def setUp(self):
        self.field_ds = Field.objects.create(
            name="Data science"
        )

        self.field_m = Field.objects.create(
            name="Math and logic"
        )

        self.field_cs = Field.objects.create(
            name="Computer sciense"
        )

        self.field_e = Field.objects.create(
            name="Engineering"
        )

        self.specialization_ec = Specialization.objects.create(
            name="Economic cybernetics",
            description="Economic systems, mathematical modeling"
        )

        self.course_ul = Course.objects.create(
            title="Unsupervised learning",
        )
        self.course_ul.fields.set([self.field_ds])

        self.group_ie1 = UniversityGroup.objects.create(
            short_name="IE-401",
            specialization=self.specialization_ec
        )

        self.student_dk = get_user_model().objects.create(
            username="dianakarpenko",
            first_name="Diana",
            last_name="Karpenko",
            group=self.group_ie1,
            password="hellogorgeous"
        )
        self.student_dk.courses.set([self.course_ul])

    def test_course_create_form(self):

        form_data = {
            "title": "Supervised learning",
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

        form_data = {
            "fields": [self.field_ds, self.field_m]
        }

        form = CourseUpdateFieldsForm(data=form_data)

        self.assertTrue(form.is_valid())
        case = form.save()
        self.assertEqual(form_data["fields"], list(case.fields.all()))

    def test_course_update_form_with_more_than_3_fields(self):

        form_data = {
            "fields": [
                self.field_ds, self.field_m, self.field_cs, self.field_e
            ]
        }

        form = CourseUpdateFieldsForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_student_create_form(self):

        form_data = {
            "username": "mariasamkova",
            "first_name": "Maria",
            "last_name": "Samkova",
            "group": self.group_ie1,
            "password1": "hellobeautiful",
            "password2": "hellobeautiful",
        }

        form = StudentCreationForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_student_create_form_with_existing_full_name(self):

        form_data = {
            "username": "mariasamkova",
            "first_name": "Diana",
            "last_name": "Karpenko",
            "group": self.group_ie1,
            "password1": "hellobeautiful",
            "password2": "hellobeautiful",
        }

        form = StudentCreationForm(data=form_data)

        self.assertFalse(form.is_valid())

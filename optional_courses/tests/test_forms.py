from django.test import TestCase

from optional_courses.forms import (
    CourseCreateForm,
    CourseUpdateFieldsForm,
    StudentCreationForm,
    StudentUpdateForm
)

from . import create_initial_data


class FormTests(TestCase):

    def setUp(self):
        create_initial_data(self)

    def test_course_create_form(self):

        form_data = {
            "title": "Supervised learning",
            "fields": [self.field_1, self.field_2],
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
                self.field_1, self.field_2, self.field_3, self.field_4
            ],
        }

        form = CourseCreateForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_course_update_fields_form(self):

        form_data = {
            "fields": [self.field_1, self.field_2]
        }

        form = CourseUpdateFieldsForm(data=form_data, instance=self.course_1)

        self.assertTrue(form.is_valid())
        form.save()
        self.assertEqual(
            form_data["fields"],
            list(self.course_1.fields.all())
        )

    def test_course_update_form_with_more_than_3_fields(self):

        form_data = {
            "fields": [
                self.field_1, self.field_2, self.field_3, self.field_4
            ]
        }

        form = CourseUpdateFieldsForm(data=form_data, instance=self.course_1)

        self.assertFalse(form.is_valid())

    def test_student_create_form(self):

        form_data = {
            "username": "dariasamkova",
            "first_name": "Daria",
            "last_name": "Samkova",
            "group": self.group_1,
            "password1": "hellobeautiful",
            "password2": "hellobeautiful",
        }

        form = StudentCreationForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_student_creation_form_lowercase_names(self):

        form_data = {
            "username": "dariasamkova",
            "first_name": "daria",
            "last_name": "samkova",
            "group": self.group_1,
            "password1": "hellobeautiful",
            "password2": "hellobeautiful",
        }

        form = StudentCreationForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["first_name"], "Daria")
        self.assertEqual(form.cleaned_data["last_name"], "Samkova")

    def test_student_create_form_with_existing_full_name(self):

        form_data = {
            "username": "mariasamkova",
            "first_name": "Diana",
            "last_name": "Karpenko",
            "group": self.group_1,
            "password1": "hellobeautiful",
            "password2": "hellobeautiful",
        }

        form = StudentCreationForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_student_update_form(self):

        form_data = {
            "first_name": self.student_1.first_name,
            "last_name": self.student_1.last_name,
            "group": self.group_2,
        }

        form = StudentUpdateForm(data=form_data, instance=self.student_1)

        self.assertTrue(form.is_valid())
        form.save()
        self.assertEqual(form_data["group"], self.student_1.group)

    def test_student_update_form_existing_full_name(self):

        form_data = {
            "first_name": "Kateryna",
            "last_name": "Vasylieva",
            "group": self.student_1.group,
        }

        form = CourseUpdateFieldsForm(data=form_data, instance=self.course_1)

        self.assertFalse(form.is_valid())

    def test_student_update_form_lowercase_names(self):

        form_data = {
            "first_name": "ariana",
            "last_name": "zavalska",
            "group": self.student_1.group,
        }

        form = StudentUpdateForm(data=form_data, instance=self.student_1)

        self.assertTrue(form.is_valid())
        form.save()
        self.assertEqual(self.student_1.first_name, "Ariana")
        self.assertEqual(self.student_1.last_name, "Zavalska")

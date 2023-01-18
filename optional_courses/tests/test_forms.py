from django.test import TestCase

from optional_courses.forms import CourseCreateForm, CourseUpdateFieldsForm
from optional_courses.models import Field, Course


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

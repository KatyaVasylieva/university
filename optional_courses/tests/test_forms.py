from django.test import TestCase

from optional_courses.forms import CourseCreateForm
from optional_courses.models import Field, Course


class FormTests(TestCase):

    def test_course_create_form(self):
        field_ds = Field.objects.create(
            name="Data science"
        )

        field_m = Field.objects.create(
            name="Math and logic"
        )

        form_data = {
            "title": "Unsupervised learning",
            "fields": [field_ds, field_m],
        }

        form = CourseCreateForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["title"], form_data["title"])
        self.assertEqual(
            list(form.cleaned_data["fields"]),
            form_data["fields"]
        )

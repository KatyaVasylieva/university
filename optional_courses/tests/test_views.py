from django.contrib.auth import get_user_model
from django.test import TestCase, Client

from django.urls import reverse

from optional_courses.models import (
    Specialization,
    Field,
    Course,
    UniversityGroup
)
from . import create_initial_data


class PublicViewsTests(TestCase):

    def test_index_login_required(self):
        index_url = reverse("optional-courses:index")
        self.client = Client()
        response = self.client.get(index_url)

        self.assertEqual(response.status_code, 302)


class PrivateViewsTests(TestCase):

    def setUp(self):

        create_initial_data(self)

        self.user = self.student_3
        self.client = Client()
        self.client.force_login(self.user)

    def test_index_correct_object_counting(self):
        index_url = reverse("optional-courses:index")
        response = self.client.get(index_url)
        count_db_objects = {
            "fields": Field.objects.count(),
            "courses": Course.objects.count(),
            "specializations": Specialization.objects.count(),
            "groups": UniversityGroup.objects.count(),
            "students": get_user_model().objects.count(),
        }

        self.assertEqual(
            response.context["num_fields"],
            count_db_objects["fields"]
        )

        self.assertEqual(
            response.context["num_courses"],
            count_db_objects["courses"]
        )

        self.assertEqual(
            response.context["num_specializations"],
            count_db_objects["specializations"]
        )

        self.assertEqual(
            response.context["num_university_groups"],
            count_db_objects["groups"]
        )

        self.assertEqual(
            response.context["num_students"],
            count_db_objects["students"]
        )

        self.assertEqual(
            response.context["num_visits"],
            1
        )

    def test_toggle_course_assignment_view(self):

        response = self.client.get(
            reverse(
                "optional-courses:course-detail",
                kwargs={"pk": self.course_1.pk}
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Assign me to this course", html=True)

        self.client.get(reverse(
            "optional-courses:course-detail",
            kwargs={"pk": self.course_1.pk}
        ) + "toggle-course-assignment/")

        response_after_assign = self.client.get(
            reverse(
                "optional-courses:course-detail",
                kwargs={"pk": self.course_1.pk}
            )
        )
        self.assertTrue(self.user in self.course_1.students.all())
        self.assertContains(
            response_after_assign, "Remove me from this course", html=True
        )

        self.client.get(
            reverse(
                "optional-courses:course-detail",
                kwargs={"pk": self.course_1.pk}
            ) + "toggle-course-assignment/"
        )

        response_after_remove = self.client.get(
            reverse(
                "optional-courses:course-detail",
                kwargs={"pk": self.course_1.pk}
            )
        )
        self.assertFalse(self.user in self.course_1.students.all())
        self.assertContains(
            response_after_remove,
            "Assign me to this course",
            html=True
        )

    def test_toggle_course_assignment_view_with_non_existing_course(self):

        non_existing_id = Course.objects.latest("id").id + 1

        response = self.client.get(
            reverse(
                "optional-courses:course-detail",
                kwargs={"pk": non_existing_id}
            )
        )

        self.assertEqual(response.status_code, 404)

    def test_course_list_view_search_by_title(self):
        form_data = {
            "title": "m"
        }
        response = self.client.get(
            reverse("optional-courses:course-list")
            + f"?title={form_data['title']}"
        )
        expected_queryset = Course.objects.filter(
            title__icontains=form_data["title"]
        )

        self.assertQuerysetEqual(
            list(response.context["course_list"]),
            list(expected_queryset)
        )

    def test_student_list_view_search_by_username(self):
        form_data = {
            "username": "ka"
        }
        response = self.client.get(
            reverse("optional-courses:student-list")
            + f"?username={form_data['username']}"
        )
        expected_queryset = get_user_model().objects.filter(
            username__icontains=form_data["username"]
        )

        self.assertQuerysetEqual(
            list(response.context["student_list"]),
            list(expected_queryset)
        )

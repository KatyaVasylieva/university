from django.contrib.auth import get_user_model
from django.test import TestCase, Client

from django.urls import reverse

from optional_courses.models import Specialization, Field, Course,\
    UniversityGroup


class PublicViewsTests(TestCase):

    def test_index_login_required(self):
        index_url = reverse("optional_courses:index")
        self.client = Client()
        response = self.client.get(index_url)

        self.assertEqual(response.status_code, 302)


class PrivateViewsTests(TestCase):

    def setUp(self):

        self.specialization_ec = Specialization.objects.create(
            name="Economic cybernetics",
            description="Economic systems, mathematical modeling"
        )

        self.specialization_cs = Specialization.objects.create(
            name="Computer science",
            description="Information systems, programming"
        )

        self.group_ie1 = UniversityGroup.objects.create(
            short_name="IE-401",
            specialization=self.specialization_ec
        )

        self.group_ie2 = UniversityGroup.objects.create(
            short_name="IE-402",
            specialization=self.specialization_ec
        )

        self.field_ds = Field.objects.create(
            name="Data science"
        )

        self.field_m = Field.objects.create(
            name="Math and logic"
        )

        self.course_ul = Course.objects.create(
            title="Unsupervised learning"
        )
        self.course_ul.field.set([self.field_ds])

        self.course_cg = Course.objects.create(
            title="Combinatorial game theory"
        )
        self.course_cg.field.set([self.field_m])

        self.student_ms = get_user_model().objects.create(
            username="mariasamkova",
            first_name="Maria",
            last_name="Samkova",
            group=self.group_ie1,
            password="hellobeautiful"
        )
        self.student_ms.courses.set([self.course_ul])

        self.student_dk = get_user_model().objects.create(
            username="dianakarpenko",
            first_name="Diana",
            last_name="Karpenko",
            group=self.group_ie2,
            password="hellogorgeous"
        )
        self.student_dk.courses.set([self.course_ul, self.course_cg])

        self.user = get_user_model().objects.create(
            username="katerynavasylieva",
            first_name="Kateryna",
            last_name="Vasylieva",
            group=self.group_ie1,
            password="testuserpassword"
        )
        self.client = Client()
        self.client.force_login(self.user)

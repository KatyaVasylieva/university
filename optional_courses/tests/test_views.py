from django.test import TestCase, Client

from django.urls import reverse


class PublicViewsTests(TestCase):

    def test_index_login_required(self):
        index_url = reverse("optional_courses:index")
        self.client = Client()
        response = self.client.get(index_url)

        self.assertEqual(response.status_code, 302)

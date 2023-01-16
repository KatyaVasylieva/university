from django.urls import path

from optional_courses.views import index

urlpatterns = [
    path("", index, name="index")
]

app_name = "optional_courses"

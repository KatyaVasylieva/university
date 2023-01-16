from django.urls import path

from optional_courses.views import index, FieldListView

urlpatterns = [
    path("", index, name="index"),
    path("fields/", FieldListView.as_view(), name="field-list")
]

app_name = "optional_courses"

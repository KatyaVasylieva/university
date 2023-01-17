from django.urls import path

from optional_courses.views import index, FieldListView, FieldDetailView

urlpatterns = [
    path("", index, name="index"),
    path("fields/", FieldListView.as_view(), name="field-list"),
    path("fields/<int:pk>/", FieldDetailView.as_view(), name="field-detail")
]

app_name = "optional_courses"

from django.urls import path

from optional_courses.views import (
    index,
    FieldListView,
    FieldDetailView,
    CourseListView,
    CourseDetailView,
    toggle_course_assignment,
    CourseCreateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("fields/", FieldListView.as_view(), name="field-list"),
    path("fields/<int:pk>/", FieldDetailView.as_view(), name="field-detail"),
    path("courses/", CourseListView.as_view(), name="course-list"),
    path(
        "courses/<int:pk>/",
        CourseDetailView.as_view(),
        name="course-detail"
    ),
    path(
        "courses/<int:pk>/toggle-course-assignment/",
        toggle_course_assignment,
        name="toggle-course-assignment"
    ),
    path(
        "courses/create/",
        CourseCreateView.as_view(),
        name="course-create"
    )
]

app_name = "optional_courses"

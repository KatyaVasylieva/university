from django.urls import path

from optional_courses.views import (
    index,
    FieldListView,
    FieldDetailView,
    CourseListView,
    CourseDetailView,
    toggle_course_assignment,
    CourseCreateView,
    CourseFieldsUpdateView,
    CourseDeleteView,
    SpecializationListView,
    SpecializationDetailView,
    UniversityGroupDetailView,
    StudentListView,
    StudentDetailView,
    StudentCreateView,
    StudentUpdateView,
    StudentDeleteView,
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
        "courses/create/", CourseCreateView.as_view(), name="course-create"
    ),
    path(
        "courses/<int:pk>/update/",
        CourseFieldsUpdateView.as_view(),
        name="course-update"
    ),
    path(
        "courses/<int:pk>/delete/",
        CourseDeleteView.as_view(),
        name="course-delete"
    ),
    path(
        "specializations/",
        SpecializationListView.as_view(),
        name="specialization-list"
    ),
    path(
        "specializations/<int:pk>/",
        SpecializationDetailView.as_view(),
        name="specialization-detail"
    ),
    path(
        "groups/<int:pk>/",
        UniversityGroupDetailView.as_view(),
        name="group-detail"
    ),
    path("students/", StudentListView.as_view(), name="student-list"),
    path(
        "students/<int:pk>/",
        StudentDetailView.as_view(),
        name="student-detail"
    ),
    path(
        "students/create/",
        StudentCreateView.as_view(),
        name="student-create"
    ),
    path(
        "students/<int:pk>/update/",
        StudentUpdateView.as_view(),
        name="student-update"
    ),
    path(
        "students/<int:pk>/delete/",
        StudentDeleteView.as_view(),
        name="student-delete"
    )
]

app_name = "optional_courses"

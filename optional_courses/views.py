from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from optional_courses.models import Field, Course, Specialization, \
    UniversityGroup


@login_required
def index(request):
    """View function for the home page of the site."""

    num_fields = Field.objects.count()
    num_courses = Course.objects.count()
    num_specializations = Specialization.objects.count()
    num_university_groups = UniversityGroup.objects.count()
    num_students = get_user_model().objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_fields": num_fields,
        "num_courses": num_courses,
        "num_specializations": num_specializations,
        "num_university_groups": num_university_groups,
        "num_students": num_students,
        "num_visits": num_visits + 1,
    }

    return render(request, "optional_courses/index.html", context=context)


class FieldListView(LoginRequiredMixin, generic.ListView):
    model = Field


class FieldDetailView(LoginRequiredMixin, generic.DetailView):
    model = Field


class CourseListView(LoginRequiredMixin, generic.ListView):
    model = Course
    paginate_by = 5

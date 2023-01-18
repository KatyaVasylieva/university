from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic

from optional_courses.forms import CourseCreateForm
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
    queryset = Field.objects.annotate(num_courses=Count("courses"))


class FieldDetailView(LoginRequiredMixin, generic.DetailView):
    queryset = Field.objects.prefetch_related("courses__students")


class CourseListView(LoginRequiredMixin, generic.ListView):
    queryset = Course.objects.prefetch_related("fields")
    paginate_by = 5


class CourseDetailView(LoginRequiredMixin, generic.DetailView):
    queryset = Course.objects.prefetch_related("fields")


class CourseCreateView(LoginRequiredMixin, generic.CreateView):
    model = Course
    form_class = CourseCreateForm


@login_required
def toggle_course_assignment(request, pk):
    student = get_user_model().objects.get(id=request.user.id)
    if Course.objects.get(id=pk) in student.courses.all():
        student.courses.remove(pk)
    else:
        student.courses.add(pk)

    return HttpResponseRedirect(
        reverse("optional_courses:course-detail", args=[pk])
    )

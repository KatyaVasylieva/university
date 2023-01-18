from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from optional_courses.forms import CourseCreateForm, CourseUpdateFieldsForm, CourseTitleSearchForm
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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CourseListView, self).get_context_data(**kwargs)
        title = self.request.GET.get("title", "")

        context["search_form"] = CourseTitleSearchForm(
            initial={"title": title}
        )

        return context

    def get_queryset(self):
        queryset = Course.objects.all()

        title = self.request.GET.get("title")

        if title:
            return queryset.filter(title__icontains=title)

        return queryset


class CourseDetailView(LoginRequiredMixin, generic.DetailView):
    queryset = Course.objects.prefetch_related("fields")


class CourseCreateView(LoginRequiredMixin, generic.CreateView):
    model = Course
    form_class = CourseCreateForm


class CourseFieldsUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Course
    form_class = CourseUpdateFieldsForm


class SpecializationListView(LoginRequiredMixin, generic.ListView):
    queryset = Specialization.objects.annotate(num_groups=Count("groups"))


class SpecializationDetailView(LoginRequiredMixin, generic.DetailView):
    model = Specialization


class UniversityGroupDetailView(LoginRequiredMixin, generic.DetailView):
    model = UniversityGroup
    template_name = "optional_courses/group_detail.html"


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

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from optional_courses.models import Field, Course, UniversityGroup


class CourseCreateForm(forms.ModelForm):
    fields = forms.ModelMultipleChoiceField(
        queryset=Field.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Course
        fields = "__all__"

    def clean_fields(self):
        return validate_course_fields(self.cleaned_data["fields"])


class CourseUpdateFieldsForm(forms.ModelForm):
    fields = forms.ModelMultipleChoiceField(
        queryset=Field.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Course
        fields = ["fields"]

    def clean_fields(self):
        return validate_course_fields(self.cleaned_data["fields"])


class CourseTitleSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Start typing the course title here"}
        )
    )


class StudentCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "group",
        )

    def clean_first_name(self):
        return case_insensitivity_for_student_names(
            self.cleaned_data["first_name"]
        )

    def clean_last_name(self):
        return case_insensitivity_for_student_names(
            self.cleaned_data["last_name"]
        )


class StudentUpdateForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "group"]

    def clean_first_name(self):
        return case_insensitivity_for_student_names(
            self.cleaned_data["first_name"]
        )

    def clean_last_name(self):
        return case_insensitivity_for_student_names(
            self.cleaned_data["last_name"]
        )


class StudentUsernameSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Start typing the student username here"}
        )
    )


def validate_course_fields(fields):
    if len(fields) > 3:
        raise ValidationError("Ensure to include no more than 3 fields")
    return fields


def case_insensitivity_for_student_names(name):
    name_clean = name[0].upper() + name[1:]
    return name_clean

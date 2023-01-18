from django import forms
from django.core.exceptions import ValidationError

from optional_courses.models import Field, Course


class CourseCreateForm(forms.ModelForm):
    fields = forms.ModelMultipleChoiceField(
        queryset=Field.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Course
        fields = "__all__"


class CourseUpdateFieldsForm(forms.ModelForm):
    fields = forms.ModelMultipleChoiceField(
        queryset=Field.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Course
        fields = ["fields"]


def validate_course_fields(fields):
    if len(fields) > 3:
        raise ValidationError("Ensure to include no more than 3 fields")
    return fields

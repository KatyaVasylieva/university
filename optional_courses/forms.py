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


def validate_course_fields(fields):
    if len(fields) > 3:
        raise ValidationError("Ensure to include no more than 3 fields")
    return fields

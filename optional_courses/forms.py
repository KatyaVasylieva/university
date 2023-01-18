from django import forms

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

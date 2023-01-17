from django import forms

from optional_courses.models import Field, Course


class CourseCreateForm(forms.ModelForm):
    field = forms.ModelMultipleChoiceField(
        queryset=Field.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Course
        fields = "__all__"

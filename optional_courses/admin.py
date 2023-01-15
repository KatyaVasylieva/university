from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from optional_courses.models import Student, UniversityGroup,\
    Course, Specialization, Field


@admin.register(Student)
class StudentAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("group",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("group",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "group",
                    )
                },
            ),
        )
    )


@admin.register(UniversityGroup)
class StudentGroupAdmin(admin.ModelAdmin):
    search_fields = ("short_name",)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_filter = ("field",)


admin.site.register(Specialization)
admin.site.register(Field)

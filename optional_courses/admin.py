from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from optional_courses.models import Student


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

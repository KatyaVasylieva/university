from django.contrib.auth.models import AbstractUser
from django.db import models


class Specialization(models.Model):
    name = models.CharField(max_length=63, unique=True)
    description = models.TextField()

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Field(models.Model):
    name = models.CharField(max_length=63, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class UniversityGroup(models.Model):
    short_name = models.CharField(max_length=7, unique=True)
    specialization = models.ForeignKey(
        Specialization,
        on_delete=models.CASCADE,
        related_name="groups"
    )

    class Meta:
        ordering = ["short_name"]

    def __str__(self):
        return self.short_name


class Course(models.Model):
    title = models.CharField(max_length=255, unique=True)
    field = models.ManyToManyField(Field, related_name="courses")

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Student(AbstractUser):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    group = models.ForeignKey(
        UniversityGroup,
        on_delete=models.CASCADE,
        related_name="students"
    )
    courses = models.ManyToManyField(
        Course,
        related_name="students"
    )

    class Meta:
        ordering = ["last_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"

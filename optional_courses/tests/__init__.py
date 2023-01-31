from django.contrib.auth import get_user_model

from optional_courses.models import (
    Field,
    Course,
    Specialization,
    UniversityGroup
)


def create_initial_data(class_inst):
    class_inst.field_1 = Field.objects.create(
        name="Data science"
    )

    class_inst.field_2 = Field.objects.create(
        name="Math and logic"
    )

    class_inst.field_3 = Field.objects.create(
        name="Computer science"
    )

    class_inst.field_4 = Field.objects.create(
        name="Engineering"
    )

    class_inst.course_1 = Course.objects.create(
        title="Unsupervised learning"
    )
    class_inst.course_1.fields.set([class_inst.field_1])

    class_inst.course_2 = Course.objects.create(
        title="Combinatorial game theory"
    )
    class_inst.course_2.fields.set([class_inst.field_2])

    class_inst.specialization_1 = Specialization.objects.create(
        name="Economic cybernetics",
        description="Economic systems, mathematical modeling"
    )

    class_inst.specialization_2 = Specialization.objects.create(
        name="Computer science",
        description="Information systems, programming"
    )

    class_inst.group_1 = UniversityGroup.objects.create(
        short_name="IE-401",
        specialization=class_inst.specialization_1
    )

    class_inst.group_2 = UniversityGroup.objects.create(
        short_name="IE-402",
        specialization=class_inst.specialization_1
    )

    class_inst.student_1 = get_user_model().objects.create(
        username="mariasamkova",
        first_name="Maria",
        last_name="Samkova",
        group=class_inst.group_1,
        password="hellobeautiful"
    )
    class_inst.student_1.courses.set([class_inst.course_1])

    class_inst.student_2 = get_user_model().objects.create(
        username="dianakarpenko",
        first_name="Diana",
        last_name="Karpenko",
        group=class_inst.group_1,
        password="hellogorgeous"
    )
    class_inst.student_2.courses.set(
        [class_inst.course_1, class_inst.course_2]
    )

    class_inst.student_3 = get_user_model().objects.create(
        username="katerynavasylieva",
        first_name="Kateryna",
        last_name="Vasylieva",
        group=class_inst.group_1,
        password="hellogorgeous"
    )

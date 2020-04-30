# Generated by Django 2.2.10 on 2020-04-30 17:47

import apps.exam.models
import apps.exam.storage
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Exam",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("university", models.CharField(max_length=100)),
                ("course", models.CharField(max_length=100)),
                ("name", models.CharField(max_length=100)),
                ("teacher", models.CharField(max_length=100)),
                (
                    "style",
                    models.CharField(
                        choices=[("C", "Compact"), ("O", "Other")],
                        default="C",
                        max_length=1,
                    ),
                ),
                ("course_code", models.CharField(max_length=50)),
                ("is_paid", models.BooleanField(default=False)),
                ("date", models.DateField()),
                ("start_time", models.TimeField()),
                ("end_time", models.TimeField()),
                (
                    "pdf_normal",
                    models.FileField(
                        storage=apps.exam.storage.OverwriteStorage(),
                        upload_to=apps.exam.models.exam_normal_path,
                    ),
                ),
                (
                    "pdf_solution",
                    models.FileField(
                        storage=apps.exam.storage.OverwriteStorage(),
                        upload_to=apps.exam.models.exam_solution_path,
                    ),
                ),
                (
                    "tex_file",
                    models.FileField(
                        storage=apps.exam.storage.OverwriteStorage(),
                        upload_to=apps.exam.models.exam_tex_path,
                    ),
                ),
                (
                    "language",
                    models.CharField(
                        choices=[("E", "English"), ("S", "Spanish")],
                        default="E",
                        max_length=1,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "image",
                    models.ImageField(
                        storage=apps.exam.storage.OverwriteStorage(),
                        upload_to=apps.exam.models.image_path,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Topic",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, unique=True)),
                ("hidden", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="Problem",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("name", models.CharField(max_length=100)),
                ("author", models.CharField(max_length=100)),
                ("content", models.CharField(max_length=50000)),
                (
                    "tex_file",
                    models.FileField(
                        storage=apps.exam.storage.OverwriteStorage(),
                        upload_to=apps.exam.models.problem_tex_path,
                    ),
                ),
                (
                    "pbtex_file",
                    models.FileField(
                        storage=apps.exam.storage.OverwriteStorage(),
                        upload_to=apps.exam.models.problem_pbtex_path,
                    ),
                ),
                (
                    "pdf",
                    models.FileField(
                        storage=apps.exam.storage.OverwriteStorage(),
                        upload_to=apps.exam.models.problem_pdf_path,
                    ),
                ),
                ("cost", models.IntegerField(default=50)),
                ("validated", models.BooleanField(default=False)),
                ("topics", models.ManyToManyField(to="exam.Topic")),
            ],
        ),
    ]
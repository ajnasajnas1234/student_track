# Generated by Django 4.2.1 on 2023-09-13 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hod", "0011_remove_course_no_of_teachers_course_teachers"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="course",
            name="Divisions",
        ),
        migrations.RemoveField(
            model_name="course",
            name="No_of_students",
        ),
        migrations.RemoveField(
            model_name="course",
            name="Teachers",
        ),
        migrations.AddField(
            model_name="course",
            name="Description",
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
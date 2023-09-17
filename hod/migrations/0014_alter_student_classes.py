# Generated by Django 4.2.1 on 2023-09-14 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hod", "0013_rename_class_student_classes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="Classes",
            field=models.CharField(
                choices=[("hifz", "HIFZ"), ("dowra", "DOWRA")],
                max_length=100,
                null=True,
            ),
        ),
    ]
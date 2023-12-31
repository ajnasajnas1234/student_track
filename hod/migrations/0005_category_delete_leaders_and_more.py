# Generated by Django 4.2.1 on 2023-08-12 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hod", "0004_rename_students_student"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Category", models.CharField(max_length=200, null=True)),
                ("Status", models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name="Leaders",
        ),
        migrations.RenameField(
            model_name="department",
            old_name="Department_name",
            new_name="Teacher_name",
        ),
        migrations.RemoveField(
            model_name="department",
            name="Department_description",
        ),
        migrations.RemoveField(
            model_name="department",
            name="Status",
        ),
        migrations.AddField(
            model_name="department",
            name="Classes",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="department",
            name="Contact_no",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="department",
            name="Department",
            field=models.CharField(max_length=100, null=True),
        ),
    ]

# Generated by Django 4.2.1 on 2023-08-12 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Students",
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
                ("Admission_no", models.IntegerField(null=True, unique=True)),
                ("Student_name", models.CharField(max_length=100, null=True)),
                ("Address", models.CharField(max_length=100, null=True)),
                ("Place", models.CharField(max_length=100, null=True)),
                ("Post", models.CharField(max_length=100, null=True)),
                ("District", models.CharField(max_length=100, null=True)),
                ("State", models.CharField(max_length=100, null=True)),
                ("Pin_code", models.IntegerField(null=True)),
                ("date_of_birth", models.DateField(null=True)),
                ("Place_of_birth", models.CharField(max_length=100, null=True)),
                ("Adhar_no", models.IntegerField(null=True)),
                ("Father_name", models.CharField(max_length=100, null=True)),
                ("Father_no", models.IntegerField(null=True, unique=True)),
                ("Father_job", models.CharField(max_length=100, null=True)),
                ("Mother_name", models.CharField(max_length=100, null=True)),
                ("Mother_no", models.IntegerField(null=True, unique=True)),
                ("Mother_job", models.CharField(max_length=100, null=True)),
                ("Guardian_name", models.CharField(max_length=100, null=True)),
                ("Guardian_no", models.IntegerField(null=True, unique=True)),
                ("Guardian_job", models.CharField(max_length=100, null=True)),
                ("Admitted_date", models.DateField(null=True)),
                ("Class", models.CharField(max_length=100, null=True)),
                ("Division", models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Teacher",
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
                ("Teacher_name", models.CharField(max_length=200, null=True)),
                ("Contact_no", models.IntegerField(null=True)),
                ("Classes", models.CharField(max_length=100, null=True)),
                ("Department", models.CharField(max_length=100, null=True)),
            ],
        ),
    ]

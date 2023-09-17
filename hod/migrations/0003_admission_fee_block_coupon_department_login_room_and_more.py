# Generated by Django 4.2.1 on 2023-08-12 15:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("hod", "0002_rename_teacher_leaders"),
    ]

    operations = [
        migrations.CreateModel(
            name="Admission_fee",
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
                ("Caution_deposit", models.IntegerField(null=True)),
                ("Registration_amenities", models.IntegerField(null=True)),
                ("Mess_advance_fee", models.IntegerField(null=True)),
                ("Amount_for_concession", models.IntegerField(null=True)),
                ("Amount_for_oec", models.IntegerField(null=True)),
                ("Amount_for_non_concession", models.IntegerField(null=True)),
                ("Status", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Block",
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
                ("Block_name", models.CharField(max_length=200, null=True)),
                ("Block_description", models.CharField(max_length=500, null=True)),
                ("Status", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Coupon",
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
                ("Type", models.CharField(max_length=200, null=True)),
                ("Amount", models.CharField(max_length=200, null=True)),
                ("Status", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Department",
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
                ("Department_name", models.CharField(max_length=200, null=True)),
                ("Department_description", models.CharField(max_length=500, null=True)),
                ("Status", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Login",
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
                ("Username", models.CharField(max_length=200, null=True)),
                ("Password", models.CharField(max_length=500, null=True)),
                ("Role", models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Room",
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
                ("Block_name", models.CharField(max_length=200, null=True)),
                ("Room_number", models.CharField(max_length=200, null=True)),
                ("Rooms_type", models.CharField(max_length=200, null=True)),
                ("Max_accommodation", models.IntegerField(null=True)),
                ("Vaccancy", models.IntegerField(blank=True, default=0, null=True)),
                ("Amount", models.IntegerField(null=True)),
                ("Status", models.CharField(max_length=100)),
                (
                    "block",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hod.block",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Room_fee",
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
                ("Month", models.CharField(max_length=200, null=True)),
                ("Amount", models.IntegerField(null=True)),
                ("Status", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Room_type",
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
                ("Room_type", models.CharField(max_length=200, null=True)),
                ("Status", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Transient",
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
                ("Name", models.CharField(max_length=200, null=True)),
                ("Message", models.CharField(max_length=500, null=True)),
                ("Role", models.CharField(max_length=100, null=True)),
                ("Status", models.CharField(max_length=100)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Room_request",
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
                ("Department_name", models.CharField(max_length=200, null=True)),
                ("Date", models.DateField(null=True)),
                ("Verification_status", models.CharField(max_length=100, null=True)),
                ("Admission_no", models.IntegerField(null=True)),
                ("Student_name", models.CharField(max_length=200, null=True)),
                ("Distance_from_home", models.IntegerField(null=True)),
                ("Status", models.CharField(max_length=100)),
                (
                    "dpt",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hod.department",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hod.students",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Room_rent",
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
                ("Payment_status", models.CharField(max_length=50, null=True)),
                ("Date", models.DateField(null=True)),
                ("Rent", models.IntegerField(default=80, null=True)),
                ("Status", models.CharField(max_length=100)),
                ("Block_name", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "Student_name",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "Room_number",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "Department_name",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("Month", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "block",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hod.block",
                    ),
                ),
                (
                    "dpt",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hod.department",
                    ),
                ),
                (
                    "room",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hod.room",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hod.students",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Room_registration",
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
                ("Name", models.CharField(max_length=200, null=True)),
                ("DOB", models.DateField(null=True)),
                ("Email", models.EmailField(max_length=254, null=True)),
                ("Phone_no", models.IntegerField(null=True)),
                ("Address", models.CharField(max_length=500, null=True)),
                ("Photo", models.ImageField(upload_to="images/")),
                ("Proof", models.ImageField(upload_to="images/")),
                ("Username", models.CharField(max_length=200, null=True)),
                ("Password1", models.CharField(max_length=200, null=True)),
                ("Password2", models.CharField(max_length=200, null=True)),
                ("Status", models.CharField(max_length=100)),
                ("Role", models.CharField(max_length=100)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="hostelmanagment_room_registrations",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="room",
            name="room",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="hod.room_type",
            ),
        ),
        migrations.CreateModel(
            name="Noticeboard",
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
                ("Title", models.CharField(max_length=200, null=True)),
                ("Content", models.CharField(max_length=500, null=True)),
                ("Date", models.DateField(null=True)),
                ("Status", models.CharField(max_length=100)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="hostelmanagment_noticeboard",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MessComplaint",
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
                ("Date", models.DateField(null=True)),
                ("Complaint_description", models.CharField(max_length=500, null=True)),
                (
                    "Reply",
                    models.CharField(default="no reply", max_length=500, null=True),
                ),
                ("Title", models.CharField(max_length=500, null=True)),
                ("Block_name", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "Student_name",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("Status", models.CharField(max_length=100)),
                (
                    "block",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hod.block",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hod.students",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Mess_track",
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
                (
                    "Mess_in_date",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "Mess_out_date",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("In_or_out", models.CharField(blank=True, max_length=50, null=True)),
                ("Time", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "Department_name",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "Student_name",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("Status", models.CharField(blank=True, max_length=100)),
                ("Date", models.CharField(blank=True, max_length=50, null=True)),
                ("Block_name", models.CharField(blank=True, max_length=200, null=True)),
                ("Mess_in_count", models.IntegerField(blank=True, null=True)),
                ("Mess_out_count", models.IntegerField(blank=True, null=True)),
                ("Students_present", models.IntegerField(blank=True, null=True)),
                ("Month", models.CharField(blank=True, max_length=200, null=True)),
                ("Fee", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "block",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hod.block",
                    ),
                ),
                (
                    "dpt",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hod.department",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hod.students",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Mess_registration",
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
                ("Name", models.CharField(max_length=200, null=True)),
                ("DOB", models.DateField(null=True)),
                ("Email", models.EmailField(max_length=254, null=True)),
                ("Phone_no", models.IntegerField(null=True)),
                ("Address", models.CharField(max_length=500, null=True)),
                ("Photo", models.ImageField(upload_to="images/")),
                ("Proof", models.ImageField(upload_to="images/")),
                ("Username", models.CharField(max_length=200, null=True)),
                ("Password1", models.CharField(max_length=200, null=True)),
                ("Password2", models.CharField(max_length=200, null=True)),
                ("Status", models.CharField(max_length=100)),
                ("Role", models.CharField(max_length=100)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Hod_student",
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
                ("Student_name", models.CharField(max_length=200, null=True)),
                ("Admission_no", models.CharField(max_length=500, null=True)),
                ("Joining_date", models.DateField(null=True)),
                ("Status", models.CharField(max_length=100)),
                (
                    "hod",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Hod_registration",
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
                ("Department_name", models.CharField(max_length=200, null=True)),
                ("Name", models.CharField(max_length=200, null=True)),
                ("Position", models.CharField(max_length=200, null=True)),
                ("Email", models.EmailField(max_length=254, null=True)),
                ("Contact_no", models.IntegerField(null=True)),
                ("Photo", models.ImageField(upload_to="images/")),
                ("Proof", models.ImageField(upload_to="images/")),
                ("Username", models.CharField(max_length=200, null=True)),
                ("Password1", models.CharField(max_length=200, null=True)),
                ("Password2", models.CharField(max_length=200, null=True)),
                ("Status", models.CharField(max_length=100)),
                ("Role", models.CharField(max_length=100)),
                (
                    "dpt",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hod.department",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="hostelmanagment_hod_registrations",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Guest_coupon",
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
                ("Guest_name", models.CharField(max_length=100, null=True)),
                ("Issued_date", models.DateField(null=True)),
                ("Type", models.CharField(max_length=200, null=True)),
                ("Amount", models.CharField(max_length=200, null=True)),
                ("Start_date", models.DateField(null=True)),
                ("End_date", models.DateField(null=True)),
                ("Status", models.CharField(max_length=100)),
                (
                    "coupon",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hod.coupon",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Feedback",
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
                ("Feedback", models.CharField(max_length=500, null=True)),
                ("Date", models.DateField(null=True)),
                ("Feedback_title", models.CharField(max_length=200, null=True)),
                (
                    "Student_name",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "Department_name",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("Status", models.CharField(max_length=100)),
                (
                    "dpt",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hod.department",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hod.students",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Expenditure",
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
                ("Year", models.IntegerField(max_length=100, null=True)),
                ("Month", models.IntegerField(max_length=100, null=True)),
                ("Total_Purchase", models.FloatField(null=True)),
                ("Opening_stock", models.FloatField(null=True)),
                ("Closing_stock", models.FloatField(null=True)),
                ("Net_purchase", models.FloatField(null=True)),
                ("Guest_coupon_charge", models.IntegerField(null=True)),
                ("Total_mess_attendance", models.IntegerField(null=True)),
                ("Total_mess_expenditure", models.FloatField(null=True)),
                ("Pay_per_expense", models.FloatField(null=True)),
                ("Salary", models.FloatField(null=True)),
                ("Pf", models.FloatField(null=True)),
                ("Mis", models.FloatField(null=True)),
                ("Audit_fee", models.FloatField(null=True)),
                ("Printing_Stationary", models.FloatField(null=True)),
                ("Other_expense", models.FloatField(null=True)),
                ("Total_fixed_expenditure", models.FloatField(null=True)),
                ("No_of_inmates", models.IntegerField(null=True)),
                ("Expense_per_inmates", models.FloatField(null=True)),
                ("Status", models.CharField(max_length=100)),
                (
                    "amt",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hod.guest_coupon",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Deallocation_Request",
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
                ("Reason", models.CharField(max_length=100, null=True)),
                ("Date", models.DateField(max_length=100, null=True)),
                ("Block_name", models.CharField(max_length=200, null=True)),
                ("Student_name", models.CharField(max_length=200, null=True)),
                ("Room_number", models.CharField(max_length=200, null=True)),
                ("Department_name", models.CharField(max_length=200, null=True)),
                ("Payment_status", models.CharField(max_length=50, null=True)),
                ("Status", models.CharField(max_length=100)),
                (
                    "block",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hod.block",
                    ),
                ),
                (
                    "dpt",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hod.department",
                    ),
                ),
                (
                    "room",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hod.room",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hod.students",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Course",
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
                ("Course_name", models.CharField(max_length=200, null=True)),
                ("Department_name", models.CharField(max_length=200, null=True)),
                ("Status", models.CharField(max_length=100)),
                (
                    "dpt",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hod.department",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Coupon_generate",
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
                ("Issued_date", models.DateField(null=True)),
                ("Amount", models.FloatField(null=True)),
                ("Type", models.CharField(max_length=200, null=True)),
                ("Student_name", models.CharField(max_length=200, null=True)),
                ("Status", models.CharField(max_length=100)),
                (
                    "coupon",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hod.coupon",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hod.students",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Complaint",
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
                ("Date", models.DateField(null=True)),
                ("Complaint_description", models.CharField(max_length=500, null=True)),
                (
                    "Reply",
                    models.CharField(default="no reply", max_length=500, null=True),
                ),
                ("Title", models.CharField(max_length=500, null=True)),
                ("Department_name", models.CharField(max_length=200, null=True)),
                ("Block_name", models.CharField(max_length=200, null=True)),
                ("Student_name", models.CharField(max_length=200, null=True)),
                ("Room_no", models.CharField(max_length=200, null=True)),
                ("Status", models.CharField(max_length=100)),
                (
                    "block",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hod.block",
                    ),
                ),
                (
                    "dpt",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hod.department",
                    ),
                ),
                (
                    "room",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hod.room",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hod.students",
                    ),
                ),
            ],
        ),
    ]

# Generated by Django 4.2.1 on 2023-08-12 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("hod", "0003_admission_fee_block_coupon_department_login_room_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Students",
            new_name="Student",
        ),
    ]

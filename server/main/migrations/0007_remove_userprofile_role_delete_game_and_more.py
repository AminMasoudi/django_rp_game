# Generated by Django 4.2.1 on 2023-06-06 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0006_rename_rolls_roles_rename_roll_userprofile_role_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofile",
            name="role",
        ),
        migrations.DeleteModel(
            name="Game",
        ),
        migrations.DeleteModel(
            name="UserProfile",
        ),
    ]

# Generated by Django 4.2.1 on 2023-06-04 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_userprofile_id_alter_userprofile_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofile",
            name="email",
        ),
    ]

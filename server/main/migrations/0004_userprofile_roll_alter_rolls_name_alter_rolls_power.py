# Generated by Django 4.2.1 on 2023-06-04 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_remove_userprofile_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="roll",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="main.rolls"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="rolls",
            name="name",
            field=models.CharField(default="No name", max_length=20),
        ),
        migrations.AlterField(
            model_name="rolls",
            name="power",
            field=models.IntegerField(default=100),
        ),
    ]

# Generated by Django 4.1.4 on 2022-12-25 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api2", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student", name="roll", field=models.IntegerField(),
        ),
    ]

# Generated by Django 4.1.6 on 2023-02-02 19:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("teams", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="team",
            name="first_cup",
            field=models.DateField(blank=True, null=True),
        ),
    ]

# Generated by Django 5.0.4 on 2024-04-07 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="Учится"),
        ),
    ]

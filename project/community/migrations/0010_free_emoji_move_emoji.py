# Generated by Django 4.2.13 on 2024-06-23 17:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("community", "0009_rename_freetag_free_freetags_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="free",
            name="emoji",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="move",
            name="emoji",
            field=models.TextField(default=""),
        ),
    ]

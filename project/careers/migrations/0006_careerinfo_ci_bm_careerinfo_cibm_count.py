# Generated by Django 4.2.13 on 2024-06-22 17:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("careers", "0005_careerinfotag_rename_place_careerinfo_field_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="careerinfo",
            name="ci_bm",
            field=models.ManyToManyField(
                blank=True, related_name="ci_bms", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="careerinfo",
            name="cibm_count",
            field=models.PositiveIntegerField(default=0),
        ),
    ]

# Generated by Django 4.2.13 on 2024-06-21 22:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("careers", "0003_careerinfo_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="careerinfo",
            name="writer",
            field=models.ForeignKey(
                default=2,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]

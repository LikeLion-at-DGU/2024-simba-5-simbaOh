# Generated by Django 5.0.3 on 2024-06-23 19:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_mentor_mentor_ship_delete_menti'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='mentor_ship',
            field=models.ManyToManyField(blank=True, related_name='menti_ship', to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 5.0.3 on 2024-06-22 17:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_mentorshiprequest_mentee_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='menti_ship',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, related_name='mentor_ship', to='accounts.profile'),
        ),
    ]

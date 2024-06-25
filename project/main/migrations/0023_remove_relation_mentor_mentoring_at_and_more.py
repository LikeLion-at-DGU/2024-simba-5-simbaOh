# Generated by Django 5.0.3 on 2024-06-25 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_relation_mentor_mentoring_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relation_mentor',
            name='mentoring_at',
        ),
        migrations.RemoveField(
            model_name='relation_mentor',
            name='state',
        ),
        migrations.AddField(
            model_name='menti',
            name='mentoring_at',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='menti',
            name='state',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]

# Generated by Django 5.2 on 2025-06-05 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote_app', '0003_codes'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardidate',
            name='cardidate_party',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cardidate',
            name='votes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

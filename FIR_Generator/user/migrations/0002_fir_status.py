# Generated by Django 4.1.7 on 2023-04-19 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fir',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]

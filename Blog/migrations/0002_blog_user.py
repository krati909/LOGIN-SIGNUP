# Generated by Django 3.2.1 on 2022-07-27 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='user',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

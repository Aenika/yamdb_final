# Generated by Django 2.2.16 on 2023-03-04 12:10

from django.db import migrations
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_merge_20221126_2014'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', users.models.CustomUserManager()),
            ],
        ),
    ]

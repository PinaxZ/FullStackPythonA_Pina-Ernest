# Generated by Django 4.2.3 on 2023-08-16 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_profile_user_celphone'),
    ]

    operations = [
        migrations.DeleteModel(
            name='profile_user',
        ),
    ]

# Generated by Django 3.2.6 on 2021-08-14 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_entry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='dated_added',
            new_name='date_added',
        ),
    ]

# Generated by Django 5.0.3 on 2024-03-29 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_branch_options_branch_colleges_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
    ]

# Generated by Django 5.0.3 on 2024-04-14 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_collegereviews_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collegereviews',
            options={},
        ),
        migrations.RemoveField(
            model_name='collegereviews',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='collegereviews',
            name='helpful',
            field=models.IntegerField(default=0),
        ),
    ]

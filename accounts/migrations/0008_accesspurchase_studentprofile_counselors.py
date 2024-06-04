# Generated by Django 5.0.3 on 2024-03-26 04:54

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_counsellorprofile_bio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessPurchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_timestamp', models.DateTimeField(auto_now_add=True)),
                ('room_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('counselor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.counsellorprofile')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.studentprofile')),
            ],
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='counselors',
            field=models.ManyToManyField(through='accounts.AccessPurchase', to='accounts.counsellorprofile'),
        ),
    ]
# Generated by Django 3.2.19 on 2023-06-19 06:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('victims', '0005_alter_all_profiles_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_profiles',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]

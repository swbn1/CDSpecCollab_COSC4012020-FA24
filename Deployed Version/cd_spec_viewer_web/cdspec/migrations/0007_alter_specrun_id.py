# Generated by Django 5.1.5 on 2025-01-30 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdspec', '0006_specrun_upload_user_string'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specrun',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

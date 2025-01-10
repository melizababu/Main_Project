# Generated by Django 5.0.2 on 2025-01-04 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('uni_rollno', models.CharField(max_length=10)),
                ('stream', models.CharField(max_length=10)),
                ('course', models.CharField(max_length=10)),
                ('semester', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'Student',
            },
        ),
    ]

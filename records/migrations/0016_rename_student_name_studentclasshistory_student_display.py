# Generated by Django 4.2.19 on 2025-04-10 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0015_studentclasshistory_student_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentclasshistory',
            old_name='student_name',
            new_name='student_display',
        ),
    ]

# Generated by Django 4.2.4 on 2023-10-02 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_record', '0002_alter_student_roll_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
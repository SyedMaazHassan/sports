# Generated by Django 3.0.8 on 2020-07-15 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0009_doctors_hospital'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='sender_patient',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='to_doctor',
        ),
        migrations.DeleteModel(
            name='department',
        ),
        migrations.RemoveField(
            model_name='fakes',
            name='USER',
        ),
        migrations.DeleteModel(
            name='appointment',
        ),
        migrations.DeleteModel(
            name='doctors',
        ),
        migrations.DeleteModel(
            name='fakes',
        ),
    ]

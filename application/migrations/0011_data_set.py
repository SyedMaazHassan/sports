# Generated by Django 3.0.8 on 2020-07-15 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('application', '0010_auto_20200715_0332'),
    ]

    operations = [
        migrations.CreateModel(
            name='data_set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Label', models.CharField(max_length=20)),
                ('EmailText', models.TextField()),
            ],
        ),
    ]

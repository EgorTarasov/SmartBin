# Generated by Django 3.0.5 on 2020-05-27 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('ip_address', models.CharField(default='192.168.0.33', max_length=15)),
                ('filled_data', models.IntegerField(default=0, max_length=1)),
            ],
        ),
    ]

# Generated by Django 2.2.3 on 2019-07-29 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='due',
            field=models.DateField(blank=True, null=True),
        ),
    ]

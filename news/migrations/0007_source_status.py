# Generated by Django 2.2.3 on 2019-07-27 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20190727_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='status',
            field=models.CharField(choices=[('G', 'good'), ('E', 'error'), ('C', 'running')], default='G', max_length=1),
        ),
    ]
# Generated by Django 2.2.3 on 2019-07-26 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20190726_1630'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=30, unique=True)),
                ('url', models.URLField()),
                ('story_url', models.URLField()),
                ('last_crawled', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Media source',
                'verbose_name_plural': 'Media sources',
                'ordering': ('name',),
            },
        ),
        migrations.AlterModelOptions(
            name='headline',
            options={'ordering': ('title',), 'verbose_name': 'Headline', 'verbose_name_plural': 'Headlines'},
        ),
        migrations.AddField(
            model_name='headline',
            name='source',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='headlines', to='news.Source'),
        ),
    ]
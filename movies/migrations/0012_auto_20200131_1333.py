# Generated by Django 2.2.5 on 2020-01-31 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_auto_20200131_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='tags',
            field=models.ManyToManyField(blank=True, to='movies.Tag', verbose_name='ジャンル'),
        ),
    ]

# Generated by Django 3.2 on 2023-01-22 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bucketorderapp', '0007_merge_20230120_0857'),
    ]

    operations = [
        migrations.AddField(
            model_name='flower',
            name='count_flower',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Кол-во в букете'),
            preserve_default=False,
        ),
    ]

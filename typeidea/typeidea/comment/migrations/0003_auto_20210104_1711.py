# Generated by Django 3.1.4 on 2021-01-04 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_comment_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='target',
            field=models.CharField(max_length=100, verbose_name='评论目标'),
        ),
    ]

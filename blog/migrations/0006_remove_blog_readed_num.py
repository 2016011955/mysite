# Generated by Django 2.0 on 2020-04-04 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blog_readed_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='readed_num',
        ),
    ]

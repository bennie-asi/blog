# Generated by Django 4.1 on 2022-08-30 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_time'], 'verbose_name': '评论', 'verbose_name_plural': '评论'},
        ),
    ]

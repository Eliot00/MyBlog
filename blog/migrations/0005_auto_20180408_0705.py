# Generated by Django 2.0.3 on 2018-04-08 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180328_1239'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-timestamp']},
        ),
    ]

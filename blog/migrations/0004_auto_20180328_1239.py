# Generated by Django 2.0.3 on 2018-03-28 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_article_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

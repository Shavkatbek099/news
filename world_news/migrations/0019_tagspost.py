# Generated by Django 4.2.4 on 2023-08-20 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world_news', '0018_featuredvideopost'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagsPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_color', models.CharField(auto_created='yellow', default='yellowgreen', max_length=20, unique=True)),
                ('urls', models.CharField(auto_created=True, max_length=375, serialize=12)),
                ('color', models.CharField(default='black', max_length=10, unique=True)),
            ],
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-14 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world_news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newstitle',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='newstitle',
            name='post_category',
            field=models.CharField(default='Game', max_length=255, verbose_name='Ichki kategoriya'),
        ),
    ]

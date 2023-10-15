# Generated by Django 4.2.4 on 2023-08-11 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryNewsTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Title in the category site')),
            ],
        ),
        migrations.CreateModel(
            name='NewsTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=350, verbose_name='Sarlavha')),
                ('photo', models.ImageField(upload_to='title/images')),
                ('description', models.TextField(verbose_name='Yangilik matni')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='world_news.categorynewstitle', verbose_name='Yangilik turi')),
            ],
        ),
    ]

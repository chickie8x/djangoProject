# Generated by Django 4.1.1 on 2022-09-10 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=500)),
                ('article_desc', models.TextField()),
                ('article_content', models.TextField()),
                ('article_slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.CharField(max_length=500)),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demoFE.article')),
            ],
        ),
    ]

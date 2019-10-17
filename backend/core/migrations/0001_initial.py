# Generated by Django 2.2.6 on 2019-10-16 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=150, verbose_name='Post Title')),
                ('post_text', models.TextField(verbose_name='Post Text')),
            ],
            options={
                'verbose_name': 'Posts',
                'verbose_name_plural': 'Posts',
                'ordering': ['post_title'],
            },
        ),
    ]

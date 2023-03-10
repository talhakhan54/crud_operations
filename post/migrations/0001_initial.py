# Generated by Django 4.1.5 on 2023-02-03 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='post/images')),
                ('data_posted', models.DateTimeField()),
            ],
        ),
    ]

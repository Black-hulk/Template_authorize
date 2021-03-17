# Generated by Django 3.0.7 on 2021-03-10 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.CharField(max_length=2)),
                ('month', models.CharField(max_length=3)),
                ('image', models.ImageField(upload_to='pics')),
                ('category', models.CharField(max_length=200)),
            ],
        ),
    ]

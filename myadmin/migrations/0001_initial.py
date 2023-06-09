# Generated by Django 4.1.7 on 2023-03-24 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tour_quote', models.CharField(max_length=200)),
                ('tour_description', models.TextField()),
                ('tour_image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]

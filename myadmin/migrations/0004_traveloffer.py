# Generated by Django 4.1.7 on 2023-03-24 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0003_package'),
    ]

    operations = [
        migrations.CreateModel(
            name='TravelOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
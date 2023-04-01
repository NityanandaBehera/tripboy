# Generated by Django 4.1.7 on 2023-03-24 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0006_traveloffer'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecentPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('post_by', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('comment', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
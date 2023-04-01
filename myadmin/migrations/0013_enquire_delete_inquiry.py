# Generated by Django 4.1.7 on 2023-03-30 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0012_inquiry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('query', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Inquiry',
        ),
    ]
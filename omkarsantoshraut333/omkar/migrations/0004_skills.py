# Generated by Django 3.1.6 on 2021-03-01 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('omkar', '0003_extra_data_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
# Generated by Django 3.0.3 on 2020-03-21 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_auto_20200321_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='login/static/45822034-167f-4e46-8876-e02177a89001'),
        ),
    ]

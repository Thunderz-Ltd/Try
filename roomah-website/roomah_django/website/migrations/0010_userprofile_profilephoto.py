# Generated by Django 3.2.3 on 2021-06-06 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20210605_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profilephoto',
            field=models.ImageField(blank=True, null=True, upload_to='profilephoto/'),
        ),
    ]

# Generated by Django 3.2.3 on 2021-06-28 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_auto_20210628_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='slug',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

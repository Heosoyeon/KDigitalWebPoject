# Generated by Django 3.2.12 on 2022-03-15 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_auto_20220314_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='voter',
            field=models.IntegerField(default=0),
        ),
    ]

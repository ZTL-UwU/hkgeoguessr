# Generated by Django 4.1.2 on 2022-10-18 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_account_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='answered',
            field=models.IntegerField(default=0),
        ),
    ]

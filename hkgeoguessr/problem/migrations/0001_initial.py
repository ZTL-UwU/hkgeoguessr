# Generated by Django 4.1.2 on 2022-10-14 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_link', models.TextField(blank=True, null=True)),
                ('rating', models.IntegerField(default=1500)),
                ('start_geo', models.IntegerField(default=0)),
                ('end_geo', models.IntegerField(default=0)),
            ],
        ),
    ]

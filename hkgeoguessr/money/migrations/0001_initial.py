# Generated by Django 4.1.2 on 2022-10-27 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Money',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField(unique=True)),
                ('video_link', models.TextField(blank=True, null=True)),
                ('rating', models.IntegerField(default=1500)),
                ('start_geo', models.IntegerField(default=0)),
                ('end_geo', models.IntegerField(default=0)),
                ('answered', models.IntegerField(default=0)),
                ('correct', models.IntegerField(default=0)),
                ('wrong', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddIndex(
            model_name='money',
            index=models.Index(fields=['pid'], name='money_money_pid_7b3b1d_idx'),
        ),
        migrations.AddIndex(
            model_name='money',
            index=models.Index(fields=['rating'], name='money_money_rating_63f795_idx'),
        ),
    ]
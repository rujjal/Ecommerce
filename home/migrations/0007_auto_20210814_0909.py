# Generated by Django 3.2.5 on 2021-08-14 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_review_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='comment',
        ),
        migrations.AddField(
            model_name='review',
            name='coment',
            field=models.TextField(blank=True),
        ),
    ]

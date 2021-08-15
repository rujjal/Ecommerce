# Generated by Django 3.2.5 on 2021-08-15 02:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0007_auto_20210814_0909'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='coment',
            new_name='comment',
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=200)),
                ('quantity', models.IntegerField(default=1)),
                ('checkout', models.BooleanField(default=False)),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-21 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='is_dislike',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]

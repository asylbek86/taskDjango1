# Generated by Django 4.2.16 on 2024-09-14 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_club',
            name='url',
            field=models.URLField(null=True),
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-26 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_violence_remove_complaint_complaint_replay_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='photo',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]

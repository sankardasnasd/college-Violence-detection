# Generated by Django 4.2.6 on 2023-10-17 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_rename_gender_authority_gendre_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('AUTHORITY', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.authority')),
            ],
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-13 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('alert', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Authority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.BigIntegerField()),
                ('gender', models.CharField(max_length=100)),
                ('age', models.DateField()),
                ('image', models.CharField(max_length=350)),
                ('e_mail', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=100)),
                ('no_of_semester', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('incident', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Security_guard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.BigIntegerField()),
                ('e_mail', models.CharField(max_length=100)),
                ('age', models.DateField()),
                ('gender', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=350)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.BigIntegerField()),
                ('e_mail', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=350)),
                ('age', models.DateField()),
                ('gender', models.CharField(max_length=100)),
                ('no_of_semester', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pincode', models.IntegerField()),
                ('parent_name', models.CharField(max_length=100)),
                ('parent_number', models.BigIntegerField()),
                ('parent_e_mail_id', models.CharField(max_length=100)),
                ('COURSE', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.course')),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.login')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.BigIntegerField()),
                ('gender', models.CharField(max_length=100)),
                ('e_mail', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=350)),
                ('age', models.DateField()),
                ('DEPARTMENT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.department')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('notification', models.CharField(max_length=100)),
                ('AUTHORITY', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.authority')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('feedback', models.CharField(max_length=100)),
                ('PARENT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.student')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='DEPARTMENT',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.department'),
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('complaint_replay', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('PARENT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.student')),
            ],
        ),
        migrations.CreateModel(
            name='checkin_chechout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin_checkout', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('status', models.CharField(max_length=100)),
                ('STUDENT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.student')),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('massege', models.CharField(max_length=100)),
                ('FROMID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fuser', to='myapp.login')),
                ('TOID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tuser', to='myapp.login')),
            ],
        ),
        migrations.AddField(
            model_name='authority',
            name='LOGIN',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.login'),
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin_checkout', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('STUDENT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.student')),
            ],
        ),
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('ALERT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.alert')),
                ('STUDENT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.student')),
            ],
        ),
    ]

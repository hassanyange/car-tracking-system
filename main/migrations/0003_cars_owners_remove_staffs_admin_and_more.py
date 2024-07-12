# Generated by Django 4.2.14 on 2024-07-12 20:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_attendancereport_attendance_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('car_name', models.CharField(max_length=255)),
                ('car_color', models.CharField(max_length=255)),
                ('car_model', models.CharField(max_length=255)),
                ('year', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Owners',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
                ('phone_number', models.CharField(max_length=12)),
                ('address', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('car', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='main.cars')),
            ],
        ),
        migrations.RemoveField(
            model_name='staffs',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='students',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='students',
            name='course',
        ),
        migrations.RemoveField(
            model_name='location',
            name='student',
        ),
        migrations.AddField(
            model_name='location',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='location',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='location',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.DeleteModel(
            name='Courses',
        ),
        migrations.DeleteModel(
            name='Staffs',
        ),
        migrations.DeleteModel(
            name='Students',
        ),
        migrations.AddField(
            model_name='location',
            name='car',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.cars'),
        ),
    ]

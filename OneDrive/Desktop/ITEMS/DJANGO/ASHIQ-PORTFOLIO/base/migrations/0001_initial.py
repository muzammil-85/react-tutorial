# Generated by Django 4.0.5 on 2022-06-11 06:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
            options={
                'verbose_name_plural': 'About',
            },
        ),
        migrations.CreateModel(
            name='ContactMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=50, null=True)),
                ('place', models.CharField(blank=True, max_length=100, null=True)),
                ('additional', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Contact',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(blank=True, max_length=100, null=True)),
                ('team', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.CharField(blank=True, max_length=50, null=True)),
                ('info', models.TextField(blank=True, null=True)),
                ('place', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Experience',
            },
        ),
        migrations.CreateModel(
            name='LC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('licence_name', models.CharField(blank=True, max_length=100, null=True)),
                ('org_name', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
            options={
                'verbose_name_plural': 'License & Certification',
            },
        ),
        migrations.CreateModel(
            name='MemorableMoment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('pic_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Memorable Moment',
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.TextField(blank=True, null=True)),
                ('quoter', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Testimonial',
            },
        ),
        migrations.CreateModel(
            name='WorkedClub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icons', models.ImageField(blank=True, null=True, upload_to='images')),
                ('club_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Worked Club',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('me_info', models.CharField(blank=True, max_length=100, null=True)),
                ('resume', models.FileField(blank=True, null=True, upload_to='upload')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Profile',
            },
        ),
    ]

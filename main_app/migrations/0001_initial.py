# Generated by Django 3.1.2 on 2021-09-08 22:28

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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.CharField(default='https://source.unsplash.com/twukN12EN7c', max_length=400)),
                ('location', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('img_one', models.ImageField(default='https://images.pexels.com/photos/4448861/pexels-photo-4448861.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260', max_length=500, upload_to='')),
                ('img_two', models.ImageField(blank=True, max_length=500, upload_to='')),
                ('img_three', models.ImageField(blank=True, max_length=500, upload_to='')),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('location', models.CharField(max_length=200)),
                ('length', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7)),
                ('elevation_gain', models.IntegerField(blank=True, default=0)),
                ('hike_rating', models.IntegerField(default=1)),
                ('hike_date', models.DateField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('hike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main_app.hike')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
# Generated by Django 4.0.5 on 2022-06-20 10:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_neighbourhood_profile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buseiness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=300)),
                ('neighbourhood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.neighbourhood')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=300)),
                ('contacts', models.CharField(max_length=300)),
                ('neighbourhood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.neighbourhood')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('content', models.TextField()),
                ('image', models.FileField(blank=True, null=True, upload_to='post_image')),
                ('neighbourhood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.neighbourhood')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Neighbourhood',
        ),
    ]

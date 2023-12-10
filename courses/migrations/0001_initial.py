# Generated by Django 4.1.7 on 2023-06-26 14:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('abstraction', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=120, null=True)),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('price', models.IntegerField(default=0)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='courses')),
                ('profs', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('subjects', models.ManyToManyField(to='courses.subject')),
            ],
        ),
    ]
# Generated by Django 4.1.7 on 2023-06-26 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_subject_siteuser_interests'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Subject',
        ),
        migrations.AlterField(
            model_name='course',
            name='subjects',
            field=models.ManyToManyField(to='accounts.subject'),
        ),
    ]

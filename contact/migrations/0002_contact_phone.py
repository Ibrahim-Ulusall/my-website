# Generated by Django 4.1.4 on 2023-06-01 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
    ]

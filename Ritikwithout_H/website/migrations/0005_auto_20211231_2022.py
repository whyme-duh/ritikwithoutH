# Generated by Django 3.2.7 on 2021-12-31 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='img',
        ),
        migrations.AddField(
            model_name='service',
            name='icon',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
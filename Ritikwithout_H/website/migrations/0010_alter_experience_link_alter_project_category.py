# Generated by Django 4.0 on 2022-01-24 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_experience_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='link',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[('CODING', 'CODING'), ('MUSIC', 'MUSIC'), ('ART', 'ART')], max_length=80, null=True),
        ),
    ]

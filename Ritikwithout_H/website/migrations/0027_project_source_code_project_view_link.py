# Generated by Django 4.1.1 on 2022-12-28 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0026_bio_delete_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='source_code',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='view_link',
            field=models.URLField(null=True),
        ),
    ]
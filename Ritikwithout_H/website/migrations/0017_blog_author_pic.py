# Generated by Django 4.0 on 2022-01-28 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_alter_blog_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author_pic',
            field=models.ImageField(default='mah.jpg', null=True, upload_to='pictures/'),
        ),
    ]
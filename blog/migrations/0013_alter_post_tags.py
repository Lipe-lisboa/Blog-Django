# Generated by Django 5.0.1 on 2024-02-01 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, default='', related_name='tag_post', to='blog.tag'),
        ),
    ]
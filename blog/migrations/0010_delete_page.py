# Generated by Django 5.0.1 on 2024-01-31 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_page_alter_category_name_alter_category_slug_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Page',
        ),
    ]

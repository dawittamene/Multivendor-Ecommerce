# Generated by Django 4.2.10 on 2024-08-01 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_alter_productimage_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
# Generated by Django 4.2.10 on 2024-07-14 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_productrating'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.TextField(null=True),
        ),
    ]

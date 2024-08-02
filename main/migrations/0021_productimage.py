# Generated by Django 4.2.10 on 2024-08-01 07:27

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_rename_customerid_customer_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', models.ImageField(null=True, upload_to='product_image/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_addresses', to='main.product')),
            ],
        ),
    ]
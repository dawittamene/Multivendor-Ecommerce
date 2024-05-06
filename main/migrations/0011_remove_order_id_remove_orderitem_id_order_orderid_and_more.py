# Generated by Django 4.2.10 on 2024-05-06 09:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_order_alter_product_category_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='id',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='id',
        ),
        migrations.AddField(
            model_name='order',
            name='OrderId',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='OrderItemId',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
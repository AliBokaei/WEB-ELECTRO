# Generated by Django 5.0.6 on 2024-06-13 22:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StoreApp', '0005_offer_header_alter_offer_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='additionaldetail',
            old_name='screen_size',
            new_name='ram_size',
        ),
        migrations.AlterField(
            model_name='additionaldetail',
            name='similar_products',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='similar_products_set', to='StoreApp.product'),
        ),
    ]
# Generated by Django 5.0.6 on 2024-06-14 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StoreApp', '0009_remove_additionaldetail_similar_products_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image_url',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]

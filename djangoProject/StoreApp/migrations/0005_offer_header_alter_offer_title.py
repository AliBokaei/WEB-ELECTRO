# Generated by Django 5.0.6 on 2024-06-13 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StoreApp', '0004_color_rename_body_review_descriptions_review_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='header',
            field=models.CharField(default=1988, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='offer',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
# Generated by Django 4.2.13 on 2024-07-10 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_aboutuspage_point_one_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='image_1',
            field=models.ImageField(null=True, upload_to='products_images'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_2',
            field=models.ImageField(null=True, upload_to='products_images'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_3',
            field=models.ImageField(null=True, upload_to='products_images'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_4',
            field=models.ImageField(null=True, upload_to='products_images'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_5',
            field=models.ImageField(null=True, upload_to='products_images'),
        ),
    ]

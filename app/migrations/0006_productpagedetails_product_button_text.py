# Generated by Django 4.2.13 on 2024-07-11 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_productpagedetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='productpagedetails',
            name='product_button_text',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

# Generated by Django 4.2.13 on 2024-07-10 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProvidingsItemPoint",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name": "Providings Item Point List",
                "verbose_name_plural": "Providings Item Point List",
            },
        ),
        migrations.AddField(
            model_name="homepageprovidingsitem",
            name="providing_points_list",
            field=models.ManyToManyField(
                blank=True,
                related_name="provinding_item_points",
                to="app.providingsitempoint",
            ),
        ),
    ]
# Generated by Django 4.2.1 on 2023-06-08 15:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("manager", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Account",
            fields=[
                ("account_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("type", models.CharField(max_length=255)),
                ("balance", models.DecimalField(decimal_places=2, max_digits=10)),
                ("interest_rate", models.DecimalField(decimal_places=2, max_digits=5)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "users",
                    models.ManyToManyField(
                        blank=True, related_name="accounts", to="manager.user"
                    ),
                ),
            ],
        ),
    ]
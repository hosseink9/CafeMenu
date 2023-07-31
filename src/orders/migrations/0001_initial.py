# Generated by Django 4.2.3 on 2023-07-31 11:17

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("foods", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
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
                (
                    "customer",
                    models.CharField(
                        max_length=15,
                        validators=[
                            django.core.validators.RegexValidator(
                                "(((\\+|00)(98))|0)?9(?P<operator>\\d{2})-?(?P<middle3>\\d{3})-?(?P<last4>\\d{4})"
                            )
                        ],
                    ),
                ),
                ("price", models.FloatField(null=True)),
                ("discount", models.FloatField(default=0.0)),
                ("date_submit", models.DateTimeField(auto_now_add=True)),
                ("is_approved", models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Table",
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
                ("name", models.CharField(max_length=25, unique=True)),
                ("is_reserved", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="OrderItem",
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
                ("quantity", models.IntegerField()),
                ("unit_price", models.FloatField()),
                ("discount", models.FloatField(default=0.0)),
                (
                    "food",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="foods.food"
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="orders.order"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="order",
            name="table",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="orders.table",
            ),
        ),
    ]

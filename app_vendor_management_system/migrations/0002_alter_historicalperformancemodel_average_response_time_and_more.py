# Generated by Django 5.0.4 on 2024-05-07 11:49

import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_vendor_management_system', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalperformancemodel',
            name='average_response_time',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='historicalperformancemodel',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='historicalperformancemodel',
            name='fulfillment_rate',
            field=models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)]),
        ),
        migrations.AlterField(
            model_name='historicalperformancemodel',
            name='on_time_delivery_rate',
            field=models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)]),
        ),
        migrations.AlterField(
            model_name='historicalperformancemodel',
            name='quality_rating_avg',
            field=models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
        migrations.AlterField(
            model_name='purchaseordermodel',
            name='delivery_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='purchaseordermodel',
            name='issue_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='purchaseordermodel',
            name='order_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='purchaseordermodel',
            name='quality_rating',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
        migrations.AlterField(
            model_name='vendormodel',
            name='average_response_time',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='vendormodel',
            name='fulfillment_rate',
            field=models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)]),
        ),
        migrations.AlterField(
            model_name='vendormodel',
            name='on_time_delivery_rate',
            field=models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)]),
        ),
        migrations.AlterField(
            model_name='vendormodel',
            name='quality_rating_avg',
            field=models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
    ]

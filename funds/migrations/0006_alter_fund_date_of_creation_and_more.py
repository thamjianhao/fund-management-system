# Generated by Django 5.1.2 on 2024-10-27 18:31

import django.core.validators
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funds', '0005_alter_fund_date_of_creation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fund',
            name='date_of_creation',
            field=models.DateField(help_text='The date when this fund was established.', verbose_name='Date of Creation'),
        ),
        migrations.AlterField(
            model_name='fund',
            name='fund_description',
            field=models.TextField(help_text="Detailed description of the fund's investment strategy and objectives.", verbose_name='Fund Description'),
        ),
        migrations.AlterField(
            model_name='fund',
            name='fund_id',
            field=models.CharField(help_text='Unique identifier for the fund. Used as the primary key.', max_length=50, primary_key=True, serialize=False, verbose_name='Fund ID'),
        ),
        migrations.AlterField(
            model_name='fund',
            name='fund_manager_name',
            field=models.CharField(help_text='The name of the person managing this fund.', max_length=255, verbose_name='Fund Manager Name'),
        ),
        migrations.AlterField(
            model_name='fund',
            name='fund_name',
            field=models.CharField(help_text='The full name of the investment fund.', max_length=255, verbose_name='Fund Name'),
        ),
        migrations.AlterField(
            model_name='fund',
            name='fund_nav',
            field=models.DecimalField(decimal_places=2, help_text='Current Net Asset Value of the fund. Must be non-negative.', max_digits=20, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Fund Net Asset Value (NAV)'),
        ),
        migrations.AlterField(
            model_name='fund',
            name='fund_performance',
            field=models.DecimalField(decimal_places=2, help_text="Fund's performance as a percentage. Must be between -100% and 1000%.", max_digits=7, validators=[django.core.validators.MinValueValidator(Decimal('-100.00')), django.core.validators.MaxValueValidator(Decimal('1000.00'))], verbose_name='Fund Performance (as a percentage)'),
        ),
    ]

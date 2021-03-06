# Generated by Django 3.1.11 on 2021-05-30 21:24
import pytest
from django.apps import apps
from django.db import migrations



class Migration(migrations.Migration):

    def insert_tax_band_data(self, schema_editor):
        TaxBand = apps.get_model("income_tax.TaxBand")
        TaxBand.objects.create(name="band_1", min=None, max=12500, percent_taxed=0)
        TaxBand.objects.create(name="band_2", min=12501, max=50000, percent_taxed=20)
        TaxBand.objects.create(name="band_3", min=50001, max=150000, percent_taxed=40)
        TaxBand.objects.create(name="band_4", min=150001, max=None, percent_taxed=45)

    dependencies = [
        ('income_tax', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(insert_tax_band_data)
    ]

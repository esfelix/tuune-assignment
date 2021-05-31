import decimal
from math import inf

from rest_framework import serializers

from apps.income_tax.models import TaxBand


class TaxBandSerializer(serializers.ModelSerializer):
    tax_due = serializers.SerializerMethodField()

    def get_tax_due(self, obj: TaxBand) -> decimal.Decimal:
        """
        Returns the amount of tax due for the given band.
        From the income and the (inclusive) band range
        """
        band_min = obj.min or 1
        band_max = obj.max or inf
        taxable_in_band = max(
            0, min(self.context["income"] - band_min, band_max - band_min) + 1
        )
        return taxable_in_band * (obj.percent_taxed / decimal.Decimal(100))

    class Meta:
        model = TaxBand
        fields = ["name", "min", "max", "percent_taxed", "tax_due"]
        read_only_fields = ["name", "min", "max", "percent_taxed", "tax_due"]


class IncomeTaxSerializer(serializers.Serializer):
    income = serializers.IntegerField()
    show_breakdown = serializers.BooleanField(default=False, required=False)
    tax_due = serializers.DecimalField(max_digits=19, decimal_places=2, read_only=True)

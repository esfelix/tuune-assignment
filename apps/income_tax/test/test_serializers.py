from decimal import Decimal

import pytest

from apps.income_tax.api.serializers import TaxBandSerializer
from apps.income_tax.models import TaxBand

pytestmark = pytest.mark.django_db

test_data = [
    (0, "band_1", Decimal(0)),
    (0, "band_2", Decimal(0)),
    (0, "band_3", Decimal(0)),
    (0, "band_4", Decimal(0)),
    (50000, "band_1", Decimal(0)),
    (50000, "band_2", Decimal(7500)),
    (50000, "band_3", Decimal(0)),
    (50000, "band_4", Decimal(0)),
    (100000, "band_1", Decimal(0)),
    (100000, "band_2", Decimal(7500)),
    (100000, "band_3", Decimal(20000)),
    (100000, "band_4", Decimal(0)),
    (150000, "band_1", Decimal(0)),
    (150000, "band_2", Decimal(7500)),
    (150000, "band_3", Decimal(40000)),
    (150000, "band_4", Decimal(0)),
    (200000, "band_1", Decimal(0)),
    (200000, "band_2", Decimal(7500)),
    (200000, "band_3", Decimal(40000)),
    (200000, "band_4", Decimal(22500)),
]


class TestTaxBandSerializer:
    @pytest.mark.parametrize("income,band,expected", test_data)
    def test_serializer_tax_band(
        self,
        income,
        band,
        expected,
    ):
        # Arrange
        tax_band = TaxBand.objects.get(name=band)

        # Act
        serializer = TaxBandSerializer(instance=tax_band, context={"income": income})

        # Assert
        assert serializer.data.get("name") == band
        assert serializer.data.get("amount_due") == expected

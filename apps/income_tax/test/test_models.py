import pytest

from apps.income_tax.models import TaxBand

pytestmark = pytest.mark.django_db


class TestTaxBandModel:
    def test_static_data(self):
        # Assert
        assert TaxBand.objects.all().count() == 4
        assert TaxBand.objects.filter(min=None, max=12500).count() == 1
        assert TaxBand.objects.filter(min=12501, max=50000).count() == 1
        assert TaxBand.objects.filter(min=50001, max=150000).count() == 1
        assert TaxBand.objects.filter(min=150001, max=None).count() == 1

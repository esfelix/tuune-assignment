from decimal import Decimal

import pytest

from apps.income_tax.tax_calculations import calculate_amount_due_in_band

tax_percentages = [0, 20, 40, 45]
taxable_amounts = [i for i in range(0, 100000, 10000)]

test_data = [(x, y) for x in taxable_amounts for y in tax_percentages]


class TestTaxCalculations:
    @pytest.mark.parametrize("taxable_amount, percent_taxed", test_data)
    def test_calculate_amount_due_in_band(self, taxable_amount, percent_taxed):
        amount_due = calculate_amount_due_in_band(taxable_amount, percent_taxed)
        assert type(amount_due) == Decimal
        assert amount_due <= taxable_amount
        assert amount_due == taxable_amount * (percent_taxed / Decimal(100))

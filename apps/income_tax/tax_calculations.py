from decimal import Decimal


def calculate_tax_due_in_band(taxable_amount: int, percent_taxed: int) -> Decimal:
    """
    Calculates the amount of tax to pay for a given band. The taxable_amount
    is the amount of the total income that falls within the given band.
    """
    return taxable_amount * (percent_taxed / Decimal(100))

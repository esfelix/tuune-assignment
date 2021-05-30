from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class TaxBand(models.Model):
    name = models.CharField(max_length=255)
    min = models.IntegerField(null=True)
    max = models.IntegerField(null=True)
    percent_taxed = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

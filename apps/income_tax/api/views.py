from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from apps.income_tax.api.serializers import IncomeTaxSerializer, TaxBandSerializer
from apps.income_tax.models import TaxBand


@api_view(http_method_names=["POST"])
def calculate_income_tax(request: Request) -> Response:
    request_data = request.data

    # Validate the input data
    income_tax_serializer = IncomeTaxSerializer(data=request_data)
    income_tax_serializer.is_valid(raise_exception=True)

    # Retrieve the tax band breakdown
    tax_band_serializer = TaxBandSerializer(
        instance=TaxBand.objects.all(),
        many=True,
        context={"income": income_tax_serializer.data["income"]},
    )
    breakdown = tax_band_serializer.data

    # Calculate the total tax
    total_tax_due = sum(tax_band["tax_due"] for tax_band in breakdown)

    # Compute response data
    response_data = {"tax_due": total_tax_due}
    if request_data.get("show_breakdown"):
        response_data["breakdown"] = tax_band_serializer.data

    return Response(response_data)

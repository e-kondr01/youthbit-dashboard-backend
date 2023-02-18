from django.shortcuts import get_object_or_404
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from analysis.plot_region_analysis import main as analyze_region
from geography.models import Region


class RegionAnalysisAPIView(APIView):
    @extend_schema(parameters=[OpenApiParameter("region_id", type=int, required=True)])
    def get(self, request, *_args, **_kwargs):
        region_id = request.query_params.get("region_id")
        region_name = get_object_or_404(Region, id=region_id).name
        resp = analyze_region(region_name)
        return Response(resp)

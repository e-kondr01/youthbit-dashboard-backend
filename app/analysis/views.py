from os.path import basename

from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from analysis.plot_region_analysis import main as analyze_region


class RegionAnalysisAPIView(APIView):
    @extend_schema(parameters=[OpenApiParameter("region", type=str, required=True)])
    def get(self, request, *_args, **_kwargs):
        region = request.query_params.get("region")
        resp = analyze_region(region)
        for region in resp:
            region[
                "plot"
            ] = "http://78.140.241.174:8100/media/plots_folder/" + basename(
                region["plot"]
            )
        return Response(resp)

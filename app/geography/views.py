from rest_framework.generics import ListAPIView

from app.geography.models import Region
from app.geography.serializers import RegionSerializer


class RegionListAPIView(ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

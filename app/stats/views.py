from rest_framework.generics import ListAPIView

from stats.models import Feature, FeatureValue
from stats.serializers import (
    ChildFeatureValueSerializer,
    FeatureSerializer,
    MapFeatureValueSerailizer,
)


class ParentFeatureListView(ListAPIView):
    queryset = Feature.objects.filter(parent_feature__isnull=True)
    serializer_class = FeatureSerializer


class ChildFeatureListView(ListAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    filterset_fields = ("parent_feature",)


class MapFeatureValueListView(ListAPIView):
    queryset = FeatureValue.objects.all()
    serializer_class = MapFeatureValueSerailizer
    filterset_fields = ("feature",)


class ChildFeatureValueListView(ListAPIView):
    queryset = FeatureValue.objects.all()
    filterset_fields = ("region", "feature__parent_feature")
    serializer_class = ChildFeatureValueSerializer

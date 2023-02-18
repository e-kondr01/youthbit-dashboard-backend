from django.db.models import Max, Min
from rest_framework.generics import ListAPIView

from stats.models import Feature, FeatureValue
from stats.serializers import (
    ChildFeatureValueSerializer,
    FeatureSerializer,
    FeatureValueSerializer,
    MapFeatureValueSerailizer,
)


class ParentFeatureListView(ListAPIView):
    queryset = Feature.objects.filter(parent_feature__isnull=True).select_related(
        "measure_unit"
    )
    serializer_class = FeatureSerializer


class ChildFeatureListView(ListAPIView):
    queryset = Feature.objects.select_related("measure_unit")
    serializer_class = FeatureSerializer
    filterset_fields = ("parent_feature",)


class MapFeatureValueListView(ListAPIView):
    queryset = FeatureValue.objects.select_related("region")
    serializer_class = MapFeatureValueSerailizer
    filterset_fields = ("feature",)

    def __init__(self, **kwargs) -> None:
        self.max_value = None
        self.min_value = None
        super().__init__(**kwargs)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        self.max_value = queryset.aggregate(Max("value"))["value__max"]
        self.min_value = queryset.aggregate(Min("value"))["value__min"]
        return super().list(request, *args, **kwargs)

    def get_serializer_context(self):
        return super().get_serializer_context() | {
            "max_value": self.max_value,
            "min_value": self.min_value,
        }


class ChildFeatureValueListView(ListAPIView):
    queryset = FeatureValue.objects.select_related("feature")
    filterset_fields = ("region", "feature__parent_feature")
    serializer_class = ChildFeatureValueSerializer


class FeatureValueListView(ListAPIView):
    queryset = FeatureValue.objects.select_related("region")
    filterset_fields = ("feature",)
    serializer_class = FeatureValueSerializer

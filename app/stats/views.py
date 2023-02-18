from django.db.models import Max, Min, QuerySet
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

    def get_serializer(self, queryset: QuerySet, **kwargs):
        max_value = queryset.aggregate(Max("value"))["value__max"]
        min_value = queryset.aggregate(Min("value"))["value__min"]
        serializer_class = self.get_serializer_class()
        context = self.get_serializer_context()
        context = context | {"max_value": max_value, "min_value": min_value}
        kwargs.setdefault("context", context)
        return serializer_class(queryset, **kwargs)


class ChildFeatureValueListView(ListAPIView):
    queryset = FeatureValue.objects.select_related("feature")
    filterset_fields = ("region", "feature__parent_feature")
    serializer_class = ChildFeatureValueSerializer


class FeatureValueListView(ListAPIView):
    queryset = FeatureValue.objects.select_related("feature__region")
    filterset_fields = "feature"
    serializer_class = FeatureValueSerializer

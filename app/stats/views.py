from rest_framework.generics import ListAPIView

from stats.models import Feature, FeatureValue
from stats.serializers import FeatureSerializer, FeatureValueSerailizer


class ParentFeatureListView(ListAPIView):
    queryset = Feature.objects.filter(parent_feature__isnull=True)
    serializer_class = FeatureSerializer


class ChildFeatureListView(ListAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    filterset_fields = ("parent_feature",)


class FeatureValueListView(ListAPIView):
    queryset = FeatureValue.objects.all()
    serializer_class = FeatureValueSerailizer
    filterset_fields = ("feature", "region", "feature__parent_feature")

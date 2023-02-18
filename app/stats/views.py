from rest_framework.generics import ListAPIView
from stats.models import Feature, FeatureValue
from stats.serializers import FeatureSerializer, FeatureValueSerailizer


class FeatureListView(ListAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer


class FeatureValueListView(ListAPIView):
    queryset = FeatureValue.objects.all()
    serializer_class = FeatureValueSerailizer
    filterset_fields = ("feature", "region")

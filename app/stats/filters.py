from django_filters import rest_framework as filters

from stats.models import FeatureValue


class ChildFeatureValueFilterSet(filters.FilterSet):
    order = filters.OrderingFilter(fields=("value",))

    class Meta:
        model = FeatureValue
        fields = ("region", "feature__parent_feature")


class FeatureValueFilterSet(filters.FilterSet):
    order = filters.OrderingFilter(fields=("value",))

    class Meta:
        model = FeatureValue
        fields = ("feature",)

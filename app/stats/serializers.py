from rest_framework import serializers
from stats.models import Feature, FeatureValue


class FeatureSerializer(serializers.ModelSerializer):
    measure_unit = serializers.CharField(source="measure_unit.name")

    class Meta:
        model = Feature
        fields = ("id", "name", "measure_unit")


class FeatureValueSerailizer(serializers.ModelSerializer):
    region_code = serializers.CharField(source="region.code")

    class Meta:
        model = FeatureValue
        fields = ("id", "value", "region_code")

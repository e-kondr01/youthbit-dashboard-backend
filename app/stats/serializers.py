from rest_framework import serializers

from stats.models import Feature, FeatureValue
from stats.utils import number_to_hex


class FeatureSerializer(serializers.ModelSerializer):
    measure_unit = serializers.CharField(source="measure_unit.name")

    class Meta:
        model = Feature
        fields = ("id", "name", "measure_unit")


class MapFeatureValueSerailizer(serializers.ModelSerializer):
    region_code = serializers.CharField(source="region.code")
    region_name = serializers.CharField(source="region.name")
    color = serializers.SerializerMethodField()

    def get_color(self, obj: FeatureValue) -> str:
        return number_to_hex(
            obj.value,
            self.context["min_value"],
            self.context["max_value"],
        )

    class Meta:
        model = FeatureValue
        fields = ("id", "value", "region_code", "color", "region_name")


class ChildFeatureValueSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="feature.name")

    class Meta:
        model = FeatureValue
        fields = ("name", "value")


class FeatureValueSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="feature.region.name")

    class Meta:
        model = FeatureValue
        fields = ("name", "value")

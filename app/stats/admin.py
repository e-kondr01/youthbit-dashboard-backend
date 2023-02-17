from django.contrib import admin
from stats.models import Feature, FeatureValue, MeasureUnit


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    pass


@admin.register(FeatureValue)
class FeatureValueAdmin(admin.ModelAdmin):
    pass


@admin.register(MeasureUnit)
class MeasureUnitAdmin(admin.ModelAdmin):
    pass

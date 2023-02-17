from django.db import models
from geography.models import Region


class MeasureUnit(models.Model):
    name = models.CharField(max_length=31, verbose_name="Название", unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Единица измерения"
        verbose_name_plural = "Единицы измерения"


class Feature(models.Model):
    name = models.CharField(max_length=511, verbose_name="Название")

    measure_unit = models.ForeignKey(
        to=MeasureUnit,
        on_delete=models.PROTECT,
        verbose_name="Единица измерения",
        related_name="features",
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Показатель"
        verbose_name_plural = "Показатели"


class FeatureValue(models.Model):
    value = models.FloatField(verbose_name="Значение")

    feature = models.ForeignKey(
        to=Feature,
        on_delete=models.CASCADE,
        verbose_name="Показатель",
        related_name="values",
    )

    region = models.ForeignKey(
        to=Region,
        on_delete=models.PROTECT,
        verbose_name="Регион",
        related_name="feature_values",
    )

    def __str__(self) -> str:
        return f"{self.feature} {self.region} {self.value}"

    class Meta:
        verbose_name = "Значение показателя"
        verbose_name_plural = "Значения показателей"

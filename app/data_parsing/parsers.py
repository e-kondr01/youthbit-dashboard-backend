import pandas as pd
from django.conf import settings
from geography.models import Region
from stats.models import Feature, FeatureValue, MeasureUnit


def parse_count_stats():
    file_path = settings.BASE_DIR / "data_parsing" / "sources" / "Форма М1 2021.xlsx"
    df = pd.read_excel(file_path, sheet_name="Р7")

    for i in df.index:
        if pd.isna(df.at[i, "Показатель"]) or df.at[i, "Показатель"].startswith(" "):
            continue

        region = df.at[i, "Регион"]
        feature = df.at[i, "Показатель"].rstrip(":")
        measure_unit = df.at[i, "Единица измерения"]
        value = df.at[i, "Значение"]

        region_db = Region.objects.filter(name=region).first()
        if not region_db:
            region_db = Region.objects.create(name=region)

        measure_unit_db = MeasureUnit.objects.filter(name=measure_unit).first()
        if not measure_unit_db:
            measure_unit_db = MeasureUnit.objects.create(name=measure_unit)

        feature_db = Feature.objects.filter(name=feature).first()
        if not feature_db:
            feature_db = Feature.objects.create(
                name=feature, measure_unit=measure_unit_db
            )

        FeatureValue.objects.create(feature=feature_db, region=region_db, value=value)

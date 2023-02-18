from typing import Dict, List

import pandas as pd
import plotly.graph_objects as go
from django.conf import settings

FOLDER_TO_SAVE_PLOTS = (
    settings.MEDIA_ROOT
    / "plots_folder"  # название папки для сохранения html файлов графиков
)

df = pd.read_csv(settings.BASE_DIR / "analysis" / "main_dataset.csv")  # датасет


def main(region: str) -> List[Dict]:
    """
    :param region: Название региона
    :return: Список блоков
    """

    forums_text, forums_status = analyze_forums(region=region)
    forums_dict = {
        "text": forums_text,
        "plot": plot_2021_forums(region=region),
        "status": forums_status,
    }

    ppl_on_unit_text, ppl_on_unit_status = analyze_ppl_on_unit(region=region)
    ppl_on_unit_dict = {
        "text": ppl_on_unit_text,
        "plot": plot_number_of_unities(region=region),
        "status": ppl_on_unit_status,
    }

    members_text, members_status = analyze_members(region=region)
    member_percent_dict = {
        "text": members_text,
        "plot": plot_members_percent(region=region),
        "status": members_status,
    }

    fin_text, fin_status = analyze_money(region=region)
    finances_dict = {
        "text": fin_text,
        "plot": plot_finance_on_com(region=region),
        "status": fin_status,
    }

    return [forums_dict, ppl_on_unit_dict, member_percent_dict, finances_dict]


def plot_2021_forums(region: str):
    """
    Построение графика количества форумов в РФ и в регионе

    :param region: Название региона

    :return: Путь до сохраненного html графика
    """
    fig = go.Figure(
        go.Histogram(
            x=df["Количество форумов за 2021"],
            xbins=dict(size=5),
            name="Распределение кол-ва<br>форумов по РФ",
        )
    )

    temp_row = df[df["Регион"] == region]
    fig.add_trace(
        go.Scatter(
            x=temp_row["Количество форумов за 2021"],
            y=[10],
            name=f"{region}",
            mode="markers",
            marker={"color": "red", "symbol": "diamond", "size": 15},
        )
    )

    fig.update_layout(
        bargap=0.03,
        xaxis_range=[-5, 80],
        title="Количество проведенных форумов в 2021 году",
    )
    fig.update_xaxes(title="Количество форумов, ед.")

    cur_plot_path = FOLDER_TO_SAVE_PLOTS / "forums.html"
    fig.write_html(cur_plot_path)

    return cur_plot_path


def plot_number_of_unities(region):
    """
    График, на котором отображено сколько человек в среднем приходится в регионе на 1 молодежное объединение

    :param region:
    :return:
    """
    fig = go.Figure(
        go.Histogram(
            x=df["Численность / Кол-во рег. объединений"],
            xbins=dict(size=10000),
            name="Распределение числа людей<br>на 1 рег. объединение",
        )
    )

    temp_row = df[df["Регион"] == region]
    fig.add_trace(
        go.Scatter(
            x=temp_row,
            y=[10],
            name=f"{region}",
            mode="markers",
            marker={"color": "red", "symbol": "diamond", "size": 15},
        )
    )

    fig.update_layout(
        bargap=0.03,
        xaxis_range=[1000, 600000],
        title="Число человек на 1 региональное молодежное объединение",
    )

    cur_plot_path = FOLDER_TO_SAVE_PLOTS / "ppl_on_unit.html"
    fig.write_html(cur_plot_path)

    return cur_plot_path


def plot_members_percent(region):
    """
    график показывает какой процент людей в регионе являются членами молодежных органов

    :param region:
    :return:
    """
    fig = go.Figure(
        go.Histogram(
            x=(df["Члены рег. органов / Численность"] * 100),
            xbins=dict(size=0.5),
            name="Распределение процента людей<br>состоящих в рег. объединениях",
        )
    )

    temp_row = df[df["Регион"] == region]
    fig.add_trace(
        go.Scatter(
            x=(100 * temp_row["Члены рег. органов / Численность"]),
            y=[10],
            name=f"{region}",
            mode="markers",
            marker={"color": "red", "symbol": "diamond", "size": 15},
        )
    )

    fig.update_layout(
        bargap=0.03,
        xaxis_range=[-1, 15],
        title="Процент людей, состоящих в региональных объединениях, от численности населения региона",
    )
    fig.update_xaxes(title="Процент от численности населения региона, %")

    cur_plot_path = FOLDER_TO_SAVE_PLOTS / "member_percent.html"
    fig.write_html(cur_plot_path)

    return cur_plot_path


def plot_finance_on_com(region):
    """
    График показывает как много денег в среднем тратится на 1 организацию в регионе
    :param region:
    :return:
    """
    fig = go.Figure(
        go.Histogram(
            x=df["Деньги / 1"],
            xbins=dict(size=0.25e7),
            name="Распределение финансирования<br>на 1 структуру",
        )
    )

    temp_row = df[df["Регион"] == region]
    fig.add_trace(
        go.Scatter(
            x=temp_row["Деньги / 1"],
            y=[10],
            name=f"{region}",
            mode="markers",
            marker={"color": "red", "symbol": "diamond", "size": 15},
        )
    )

    fig.update_layout(
        bargap=0.03,
        xaxis_range=[-1e5, 0.9e8],
        title="Финансирование на единицу структуры по работе с молодежью",
    )
    fig.update_xaxes(title="Объем финансирования на 1 структуру, руб.")

    cur_plot_path = FOLDER_TO_SAVE_PLOTS / "finance.html"
    fig.write_html(cur_plot_path)

    return cur_plot_path


def analyze_forums(region, lower_bracket=-0.7, upper_bracket=0.7):
    temp_row = df[df["Регион"] == region]
    temp_val = temp_row["Количество форумов за 2021"].values[0]

    mean = df["Количество форумов за 2021"].mean()
    std = df["Количество форумов за 2021"].std()

    diff = (temp_val - mean) / std

    if lower_bracket <= diff <= upper_bracket:
        status = "ok"
        text = (
            f"В регионе {region} за 2021 было проведено {int(temp_val)} форумов. В среднем в регионах "
            f"России в 2021 проводилось по {int(mean)} форумов.\n"
            f"Показатель проведенных за год форумов для данного региона находится в норме!"
        )
    elif diff > upper_bracket:
        status = "good"
        text = (
            f"В регионе {region} за 2021 было проведено {int(temp_val)} форумов. В то же время в "
            f"регионах России в среднем было проведено по {int(mean)} форумов.\n"
            f"Данный показатель для региона {region} превышает норму!!!"
        )
    else:
        status = "bad"
        text = (
            f"В 2021 году в регионе {region} проводилось крайне мало форумов. За год было проведено "
            f"{int(temp_val)} форумов, однако среднее значение по России составляет {int(mean)}. В "
            f"данном регионе следует проводить больше форумов."
        )

    return text, status


def analyze_ppl_on_unit(region, upper_bracket=0.8, lower_bracket=-0.4):
    temp_row = df[df["Регион"] == region]
    temp_val = temp_row["Численность / Кол-во рег. объединений"].values[0]

    mean = df["Численность / Кол-во рег. объединений"].mean()
    std = df["Численность / Кол-во рег. объединений"].std()
    diff = (temp_val - mean) / std

    if lower_bracket <= diff <= upper_bracket:
        status = "ok"
        text = (
            f"В регионе {region} в среднем {int(temp_val)} человек приходится на 1 региональное "
            f"молодежное объединение. По России этот показатель в среднем составляет {int(mean)}.\n"
            f"Число человек на 1 молодежное объединение для данного региона находится в норме!"
        )
    elif diff > upper_bracket:
        status = "bad"
        text = (
            f"В регионе {region} слишком много человек приходится на 1 региональное "
            f"молодежное объединение. В среднем - {int(temp_val)} человек. В то же "
            f"время среднее значение по остальным субъектам РФ составляет {int(mean)} человек.\n"
            f"Данный показатель для региона {region} превышает норму!"
        )
    else:
        status = "good"
        text = (
            f"В регионе {region} на 1 региональное молодежное объединение приходится всего "
            f"{int(temp_val)} человек, что является хорошим показателем относительно "
            f"среднего по России - {int(mean)}!"
        )

    return text, status


def analyze_members(region, upper_bracket=0.75, lower_bracket=-0.5):
    temp_row = df[df["Регион"] == region]
    temp_val = temp_row["Члены рег. органов / Численность"].values[0] * 100

    mean = df["Члены рег. органов / Численность"].mean() * 100
    std = df["Члены рег. органов / Численность"].std() * 100
    diff = (temp_val - mean) / std

    if lower_bracket <= diff <= upper_bracket:
        status = "ok"
        text = (
            f"В регионе {region} в среднем {round(temp_val, 2)}% являются "
            f"членами региональных объединений. Данный показатель находится в "
            f"норме. По России среднее значение составляет {round(mean, 2)}%"
        )
    elif diff > upper_bracket:
        status = "good"
        text = (
            f"В регионе {region} {round(temp_val, 2)}% от населения являются членами "
            f"региональных объединений. В среднем по России этот показатель равен {round(mean, 2)}%.\n"
            f"Данный показатель для региона {region} превышает норму!"
        )
    else:
        status = "bad"
        text = (
            f"В регионе {region} всего {round(temp_val, 2)}% от населения являются членами "
            f"региональных молодежных объединений. Это крайне мало! В среднем по "
            f"России данный показатель равен {round(mean, 2)}%"
        )

    return text, status


def analyze_money(region, upper_bracket=0.6, lower_bracket=-0.2):
    temp_row = df[df["Регион"] == region]
    temp_val = temp_row["Деньги / 1"].values[0] * 100

    mean = df["Деньги / 1"].mean() * 100
    std = df["Деньги / 1"].std() * 100
    diff = (temp_val - mean) / std

    if lower_bracket <= diff <= upper_bracket:
        status = "ok"
        text = (
            f"В регионе {region} в 2021 году было потрачено {int(temp_val)} руб в "
            f"среднем на структурную единицу по работе с молодежью. Данный показатель находится в норме, "
            f"так как по России среднее значение составляет {int(mean)} руб."
        )
    elif diff > upper_bracket:
        status = "bad"
        text = (
            f"В регионе {region} {int(temp_val)} руб в среднем расходуются на одну структурную единицу "
            f"по работе с молодежью. В среднем по России этот показатель равен {int(mean)}руб.\n"
            f"Данный показатель в регионе {region} сильно превышает норму!"
        )
    else:
        status = "good"
        text = (
            f"В регионе {region} очень низкие расходы на единицу структуры по работе с молодежью: "
            f"{int(temp_val)} руб по сравнению со средним по России - {int(mean)} руб!"
        )

    return text, status

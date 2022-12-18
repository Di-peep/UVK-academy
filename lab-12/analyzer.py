import os

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import requests


DATA_LINK = "https://raw.githubusercontent.com/Vadimkin/ukrainian-air-raid-sirens-dataset/main/datasets/full_data.csv"
DATA_PATH = "./data.csv"


def download_data_if_not_exist():
    if not os.path.exists(DATA_PATH):
        data = requests.get(DATA_LINK)
        with open(DATA_PATH, "w") as file:
            file.write(data.text)


def analyze_by_week(alerts: pd.DataFrame):
    alerts_copy = alerts.copy(deep=True)
    alerts_copy["week"] = alerts_copy["Date_start"].dt.strftime('%U')

    draw_chart(alerts_copy.groupby("week").aggregate({"Date_start": "count"}))
    draw_chart(alerts_copy.groupby("week").aggregate({"Duration": "mean"}))


def analyze_by_day(alerts: pd.DataFrame):
    print("\nAlarm counter for each day of the week:")
    print(alerts.groupby(alerts["Date_start"].dt.strftime('%a'))['Duration'].count())

    print("\nThe longest alarms for every day of the week:")
    print(alerts.groupby(alerts["Date_start"].dt.strftime('%a'))['Duration'].max())


def draw_chart(alerts: pd.DataFrame):
    plt.figure()
    alerts.plot()
    plt.show()


def analyze():
    alerts = pd.read_csv(DATA_PATH, parse_dates=["started_at", "finished_at"])

    alerts["Date_start"] = pd.to_datetime(alerts["started_at"].dt.date)
    alerts["Time_start"] = alerts["started_at"].dt.time

    alerts["Date_finish"] = pd.to_datetime(alerts["finished_at"].dt.date)
    alerts["Time_finish"] = alerts["finished_at"].dt.time

    alerts["Duration"] = (alerts["finished_at"] - alerts["started_at"]) / np.timedelta64(1, 'h')

    analyze_by_week(alerts)
    analyze_by_day(alerts)


if __name__ == "__main__":
    download_data_if_not_exist()
    analyze()

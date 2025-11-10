import json
import os

import pandas as pd


def get_csv(path: str) -> list[dict]:
    """
    Принимает путь к файлу в формате csv, содержащий информацию о транзакциях,
    и возвращает список словарей с транзакциями.
    """
    if os.path.exists(path):
        if path.endswith(".csv"):
            df = pd.read_csv(path, sep=";")
            data_json = df.to_json(orient="records")
            data = json.loads(data_json)
            return data
        else:
            raise ValueError(f"File '{path}' is not a csv.")
    else:
        raise FileNotFoundError(f"File '{path}' not found.")



print(get_csv("../data/transactions.csv"))
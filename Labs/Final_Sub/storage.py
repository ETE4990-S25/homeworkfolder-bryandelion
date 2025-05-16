import os
import json
from typing import Any


def ensure_directory(path: str) -> None:
    """
    Create the directory if it doesn't exist.
    """
    os.makedirs(path, exist_ok=True)


def json_file_exists(currency_code: str, date_str: str) -> bool:
    """
    Check if the JSON file already exists for the given currency and date.
    """
    file_path = os.path.join("data", currency_code, f"{date_str}.json")
    return os.path.exists(file_path)


def save_json(currency_code: str, date_str: str, data: Any) -> None:
    """
    Save the given data to a JSON file under data/<currency_code>/<date>.json.
    """
    dir_path = os.path.join("data", currency_code)
    ensure_directory(dir_path)

    file_path = os.path.join(dir_path, f"{date_str}.json")
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=2)

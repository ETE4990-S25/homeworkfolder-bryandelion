import os
import json
import pandas as pd
from pathlib import Path

def load_currency_data(base_currency, target_currency="USD"):
    records = []
    base_path = Path(f"data/{base_currency}")

    for file in sorted(base_path.glob("*.json")):
        with open(file) as f:
            try:
                data = json.load(f)
                items = data.get("channel", {}).get("item", [])
                if isinstance(items, dict):  # single item case
                    items = [items]

                for item in items:
                    if item.get("targetCurrency") == target_currency:
                        records.append({
                            "date": pd.to_datetime(item["date"]),
                            "rate": float(item["exchangeRate"]),
                            "base": base_currency
                        })
            except Exception as e:
                print(f"Error loading {file}: {e}")

    return pd.DataFrame(records)

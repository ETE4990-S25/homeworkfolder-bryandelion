import requests
from parser import xml_to_json
from storage import save_json, file_exists
from quest_log import log

def fetch_exchange_data(base: str, date_str: str) -> str | None:
    """
    Fetches XML exchange rate data for a given base currency and date.
    """
    url = (
        "https://www.floatrates.com/historical-exchange-rates.html"
        f"?operation=rate&pb_id=7759&base={base}&date={date_str}"
    )
    try:
        response = requests.get(url, timeout=8)
        response.raise_for_status()
        return response.text
    except Exception as err:
        log(f" Failed to fetch {base} on {date_str}: {err}")
        return None

def download_exchange_day(base: str, date_str: str) -> None:
    """
    Downloads and saves exchange data if not already present.
    """
    if file_exists(base, date_str):
        log(f" Skipped {base} on {date_str} (already downloaded)")
        return

    xml_content = fetch_exchange_data(base, date_str)
    if xml_content:
        json_data = xml_to_json(xml_content)
        save_json(base, date_str, json_data)
        log(f" Saved data for {base} on {date_str}")
import threading
from datetime import timedelta
from downloader import download_day
from quest_log import log


def generate_date_range(start_date, end_date):
    """
    Yield date strings in 'YYYY-MM-DD' format from start_date to end_date (inclusive).
    """
    total_days = (end_date - start_date).days + 1
    for offset in range(total_days):
        current_date = start_date + timedelta(days=offset)
        yield current_date.strftime("%Y-%m-%d")


def download_worker(base_currency, date_list):
    """
    Worker thread that downloads exchange data for a list of dates.
    """
    for date in date_list:
        download_day(base_currency, date)


def run_threaded_downloads(base_currency, all_dates, num_threads):
    """
    Split the dates into chunks and run parallel downloads using threads.
    """
    chunk_size = max(1, len(all_dates) // num_threads)
    threads = []

    for i in range(num_threads):
        chunk = all_dates[i * chunk_size : (i + 1) * chunk_size]
        if not chunk:
            continue  # Skip empty chunks if data is imbalanced
        thread = threading.Thread(target=download_worker, args=(base_currency, chunk))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    log(f"✅ Finished downloading scrolls for {base_currency}")
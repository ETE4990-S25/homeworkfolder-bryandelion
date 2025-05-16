import random
from datetime import datetime

from config import VALID_BASES, START_DATE, THREAD_COUNT
from threader import generate_date_range, run_threaded_downloads
from quest_log import log


def start_scroll_quest():
    """
    Starts the data retrieval quest for a randomly selected base currency.
    """
    base_currency = random.choice(VALID_BASES)
    log(f" Beginning quest for base currency: {base_currency}")

    end_date = datetime.today()
    date_list = list(generate_date_range(START_DATE, end_date))

    run_threaded_downloads(base_currency, date_list, THREAD_COUNT)


if __name__ == "__main__":
    start_scroll_quest()
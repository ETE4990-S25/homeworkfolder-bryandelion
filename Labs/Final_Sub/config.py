from datetime import datetime

# List of supported currency codes
CURRENCIES = [
    "AUD", "BND", "BWP", "CAD", "CHF", "CLP", "CNY", "COP", "CZK",
    "DKK", "DZD", "EUR", "GBP", "HUF", "IDR", "ILS", "INR", "ISK",
    "KRW", "KWD", "KZT", "LKR", "LYD", "MYR", "NOK", "NPR", "NZD",
    "OMR", "PKR", "PLN", "QAR", "RUB", "SAR", "SEK", "SGD", "THB",
    "TTD", "USD", "ZAR"
]

# Exclude commonly used base currencies
EXCLUDED_BASES = {"USD", "EUR", "GBP"}

# Filtered list of valid base currencies
VALID_BASES = [code for code in CURRENCIES if code not in EXCLUDED_BASES]

# Start date for data retrieval
START_DATE = datetime(year=2011, month=5, day=4)

# Number of threads to use
THREAD_COUNT = 10
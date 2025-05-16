from load_data import load_currency_data
import pandas as pd

major_bases = ["USD", "EUR", "GBP", "JPY", "CNY"]

df_all = pd.concat([
    load_currency_data(base_currency=code)
    for code in major_bases
])

df_all.sort_values("date", inplace=True)
df_all.reset_index(drop=True, inplace=True)
# analyze_major.py

...

# Make df_all accessible for other scripts
__all__ = ["df_all"]

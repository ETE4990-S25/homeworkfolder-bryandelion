import matplotlib.pyplot as plt
import seaborn as sns

# Set consistent plotting style
sns.set(style="whitegrid", palette="muted", font_scale=1.2)


def plot_exchange_rate_trends(df_all):
    """
    Line plot showing exchange rate trends over time.
    """
    plt.figure(figsize=(12, 5))
    sns.lineplot(data=df_all, x="date", y="rate", hue="base")
    plt.title("Exchange Rate Trends (Target: USD)")
    plt.xlabel("Date")
    plt.ylabel("Exchange Rate")
    plt.legend(title="Base Currency")
    plt.show()


def plot_rolling_volatility(df_all):
    """
    Line plot showing 30-day rolling standard deviation (volatility).
    """
    volatility = df_all.copy()
    volatility["volatility"] = (
        volatility.groupby("base")["rate"]
        .transform(lambda x: x.rolling(window=30, min_periods=1).std())
    )

    plt.figure(figsize=(12, 5))
    sns.lineplot(data=volatility, x="date", y="volatility", hue="base")
    plt.title("30-Day Rolling Volatility of Major Currencies")
    plt.xlabel("Date")
    plt.ylabel("Rolling Std Dev")
    plt.show()


def plot_boxplot_exchange_rates(df_all):
    """
    Boxplot showing the distribution of exchange rates by currency.
    """
    plt.figure(figsize=(12, 5))
    sns.boxplot(data=df_all, x="base", y="rate")
    plt.title("Distribution of Exchange Rates by Base Currency (to USD)")
    plt.xlabel("Base Currency")
    plt.ylabel("Exchange Rate")
    plt.show()


def plot_correlation_heatmap(df_all):
    """
    Heatmap showing correlation between currencies based on their rates.
    """
    pivot_df = df_all.pivot_table(index="date", columns="base", values="rate")
    corr_matrix = pivot_df.corr()

    plt.figure(figsize=(12, 6))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
    plt.title("Correlation Between Base Currencies")
    plt.show()


if __name__ == "__main__":
    from analyze_major import get_major_currency_data

    df_all = get_major_currency_data()
    plot_exchange_rate_trends(df_all)
    plot_rolling_volatility(df_all)
    plot_boxplot_exchange_rates(df_all)
    plot_correlation_heatmap(df_all)

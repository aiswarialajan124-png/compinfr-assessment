#!/usr/bin/env python3
"""
Download hourly stock and plot the percentage change.

Running this script downloads five days of hourly data for five technology companies, saves it in the data folder, and saves a plot of the percentage change in the Close price in the plots folder. Run it from the root of the repository with ./stocks.py
"""
# Dates and times
import datetime as dt

# File system paths
from pathlib import Path

# Plotting
import matplotlib.pyplot as plt

# Data frames
import pandas as pd

# Yahoo Finance data
import yfinance as yf

def get_data():
    """Download five days of hourly stock data and save it to a CSV file.
    
    The file is saved in the data folder as YYYYMMDD-HHmmss.csv, using the time of the download.
    
    Returns
    -------
    pandas.DataFrame
        Hourly prices and volumnes for NVDA, AVGO, ARM, AMD, and IBM.
    """
    # Ticker symbols for the five companies
    tickers = ["NVDA", "AVGO", "ARM", "AMD", "IBM"]

    # One call for all tickers: faster than fie seperate downloads and gives a single table with the same timestamps for every company
    data = yf.download(tickers, period="5d", interval="1h", progress=False)

    # exist_ok=True so the function does not fail if the folder exists
    data_folder = Path("data")
    data_folder.mkdir(exist_ok=True)

    # Timestamp in the filename means each run creates a new file
    timestamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = data_folder / f"{timestamp}.csv"

    # Save the data, including the multi-level column headers
    data.to_csv(filename)

    return data

def plot_data():
    """Plot the percentage change in Close price from the newest data file.
    
    Reads the most recent CSV in the data folder, calculates each company's percentage change relative to its first observation, plots all five on one set of axes and saves the figure in the plots folder as YYYYMMDD-HHmmss.png (the timestamp of the CSV file).
    """
    # Newest file last, because the timestamped names sort chronologically
    csv_files = sorted(Path("data").glob("*.csv"))
    if not csv_files:
        raise FileNotFoundError("No CSV files in the data/. Run get_data() first.")
    latest_file = csv_files[-1]

    # Two header rows: price type and ticker
    prices = pd.read_csv(latest_file, header=[0, 1], index_col=0)

    # Mixed UTC offsets (clock change), so convert via UTC to New York time
    prices.index = pd.to_datetime(prices.index, utc=True).tz_convert("America/New_York")

    # Select Close only; dividing by row 0 (P_0) scales each company by its own starting pricee
    close = prices["Close"]
    pct_change = (close - close.iloc[0]) / close.iloc[0] * 100

    # Colours come from matplotlib's default cycle; line styles add a second way to tell the series apart
    line_styles = ["-", "--", "-.", ":", "-"]

    fig, ax = plt.subplots(figsize=(12, 6))
    for ticker, style in zip(pct_change.columns, line_styles):
        ax.plot(pct_change.index, pct_change[ticker], linestyle=style, label=ticker)

    start, end = pct_change.index[0], pct_change.index[-1]
    ax.set_title(
        f"Percentage change in Close price: {start:%d %B %Y} to {end:%d %B %Y}"
    )
    ax.set_xlabel("Date and time (New York time)")
    ax.set_ylabel("Change since first observation (%)")
    ax.legend(title="Company")
    ax.grid(alpha=0.3)

    # Rotate the date labels so they don't overlap
    fig.autofmt_xdate()

    # Create the plots folder if needed, then save using the CSV's timestamp
    plots_folder = Path("plots")
    plots_folder.mkdir(exist_ok=True)
    fig.savefig(plots_folder / f"{latest_file.stem}.png", dpi=150)

     # Close the figure instead of showing it: a script run from the terminal
    plt.close(fig)

# Only run when executed directly, not when imported as a module
if __name__ == "__main__":
    get_data()
    plot_data()
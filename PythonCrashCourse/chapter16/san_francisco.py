import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/san_francisco_2020.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, and high and low tempratures from this file.
    dates, highs, lows  = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[5], '%Y-%m-%d')
        try:
            high = int(row[12])
            low = int(row[14])
        except ValueError:
            print(f"Missing data for {current_date}")
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

    # Plot the high and low tempratures.
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red', alpha=0.5)
    ax.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # Format plot.
    plt.title("Daily high and low temperatures, -2020", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

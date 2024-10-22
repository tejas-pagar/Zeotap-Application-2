import matplotlib.pyplot as plt

def plot_daily_summary(summaries):
    dates = list(summaries.keys())
    avg_temps = [summaries[date]['avg_temp'] for date in dates]

    plt.plot(dates, avg_temps, marker='o')
    plt.title('Average Daily Temperature')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

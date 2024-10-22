from data_retrieval import fetch_weather
from data_processing import process_weather_data, calculate_daily_summary
from alerting import check_alerts
from visualization import plot_daily_summary
from storage import create_table, insert_daily_summary
import time
import config

def main():
    create_table()  # Initialize the database tables
    daily_data = {}

    while True:
        for city in config.CITIES:
            weather_data = fetch_weather(city)
            if weather_data:
                process_weather_data(weather_data, daily_data)
                check_alerts(weather_data)

        daily_summary = calculate_daily_summary(daily_data)
        for date, summary in daily_summary.items():
            insert_daily_summary(date, summary['avg_temp'], summary['max_temp'], summary['min_temp'], summary['dominant_condition'])

        plot_daily_summary(daily_summary)

        time.sleep(config.RETRIEVAL_INTERVAL)

if __name__ == "__main__":
    main()

import config

def check_alerts(weather_data):
    temp = weather_data['main']['temp']
    if temp > config.ALERT_THRESHOLD_TEMP:
        print(f"Alert: Temperature in {weather_data['name']} exceeded {config.ALERT_THRESHOLD_TEMP}°C!")

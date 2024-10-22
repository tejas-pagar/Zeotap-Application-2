from datetime import datetime

daily_data = {}

def process_weather_data(weather_data, daily_data):
    city = weather_data['name']
    temp = weather_data['main']['temp']
    condition = weather_data['weather'][0]['main']
    dt = datetime.fromtimestamp(weather_data['dt']).date()

    if dt not in daily_data:
        daily_data[dt] = {'temp_sum': 0, 'temp_count': 0, 'temp_max': temp, 'temp_min': temp, 'condition_count': {}}

    daily_data[dt]['temp_sum'] += temp
    daily_data[dt]['temp_count'] += 1
    daily_data[dt]['temp_max'] = max(daily_data[dt]['temp_max'], temp)
    daily_data[dt]['temp_min'] = min(daily_data[dt]['temp_min'], temp)

    if condition not in daily_data[dt]['condition_count']:
        daily_data[dt]['condition_count'][condition] = 0
    daily_data[dt]['condition_count'][condition] += 1

def calculate_daily_summary(daily_data):
    summaries = {}
    for date, data in daily_data.items():
        avg_temp = data['temp_sum'] / data['temp_count']
        dominant_condition = max(data['condition_count'], key=data['condition_count'].get)
        summaries[date] = {
            'avg_temp': avg_temp,
            'max_temp': data['temp_max'],
            'min_temp': data['temp_min'],
            'dominant_condition': dominant_condition
        }
    return summaries

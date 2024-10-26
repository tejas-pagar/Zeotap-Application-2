import matplotlib.pyplot as plt
import numpy as np

def plot_daily_summary(daily_summary, cities):
    """Plot daily summary of weather data."""
    dates = list(daily_summary.keys())
    
   
    for city in cities:
        avg_temps = [summary['avg_temp'] for summary in daily_summary.values()]
        max_temps = [summary['max_temp'] for summary in daily_summary.values()]
        min_temps = [summary['min_temp'] for summary in daily_summary.values()]

        
        plt.figure(figsize=(12, 6))
        
        
        plt.plot(dates, avg_temps, marker='o', color='blue', label=f'Average Temp in {city}', linewidth=2)
        plt.plot(dates, max_temps, marker='o', color='red', label=f'Max Temp in {city}', linewidth=2, linestyle='dashed')
        plt.plot(dates, min_temps, marker='o', color='green', label=f'Min Temp in {city}', linewidth=2, linestyle='dotted')

        
        high_temp_indices = np.where(np.array(max_temps) > 35)[0]  # Change 35 to your threshold
        plt.scatter(np.array(dates)[high_temp_indices], np.array(max_temps)[high_temp_indices], 
                    color='orange', s=100, edgecolor='black', label='High Temperatures (>35°C)', zorder=5)

    
    plt.title('Daily Weather Summary', fontsize=16)
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Temperature (°C)', fontsize=14)
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)

    
    plt.grid(visible=True, linestyle='--', alpha=0.7)
    plt.legend(fontsize=12)
    plt.tight_layout()
    
    
    plt.show()

The Weather Monitoring System is a real-time data processing system designed to continuously retrieve weather data from the OpenWeatherMap API.<br>
It monitors weather conditions in various cities and provides daily summaries, alerts based on configurable thresholds, and visualizations for better analysis.<br>
<br>
<br>
<br>
Tech Used :-<br>
Python <br>
Requests: For making API requests to OpenWeatherMap.<br>
Matplotlib: For generating visualizations.<br>
SQLite: For persisting weather data and alerts.<br>
Pandas (optional): For advanced data handling (future extensions).<br>
<br>
<br>
<br>
Features:- <br>
Fetches weather data at intervals (e.g., every 5 minutes).<br>
Aggregates daily weather data (average, max, min temperatures).<br>
Alerts when user-defined thresholds (e.g., >35°C) are breached.<br>
Visualizes weather trends and alert history.

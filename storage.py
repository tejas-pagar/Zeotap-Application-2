import sqlite3

def create_connection():
    conn = sqlite3.connect('weather_data.db')  # Create or connect to SQLite database
    return conn

def create_table():
    conn = create_connection()
    with conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS daily_weather (
                date TEXT PRIMARY KEY,
                avg_temp REAL,
                max_temp REAL,
                min_temp REAL,
                dominant_condition TEXT
            )
        ''')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS alerts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                city TEXT,
                alert_message TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
    conn.close()

def insert_daily_summary(date, avg_temp, max_temp, min_temp, dominant_condition):
    conn = create_connection()
    with conn:
        conn.execute('''
            INSERT OR REPLACE INTO daily_weather (date, avg_temp, max_temp, min_temp, dominant_condition)
            VALUES (?, ?, ?, ?, ?)
        ''', (date, avg_temp, max_temp, min_temp, dominant_condition))
    conn.close()

def insert_alert(city, alert_message):
    conn = create_connection()
    with conn:
        conn.execute('''
            INSERT INTO alerts (city, alert_message)
            VALUES (?, ?)
        ''', (city, alert_message))
    conn.close()

def get_daily_summaries():
    conn = create_connection()
    with conn:
        cursor = conn.execute('SELECT * FROM daily_weather')
        return cursor.fetchall()

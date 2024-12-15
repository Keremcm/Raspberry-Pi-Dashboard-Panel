from flask import Flask, render_template, jsonify
import psutil
import requests
import datetime
import os

app = Flask(__name__)

# OpenWeatherMap API Key and City
API_KEY = "1a44ca0976662f6f21b9cab1af1db067"
CITY = "Bursa, Mudanya"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/system_info')
def system_info():
    # Gather system information
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    try:
        temp = psutil.sensors_temperatures().get('cpu-thermal', [{}])[0].get('current', None)
    except Exception:
        temp = None

    return jsonify({
        'cpu_usage': cpu_usage,
        'ram_usage': ram_usage,
        'disk_usage': disk_usage,
        'temperature': temp
    })

@app.route('/api/weather')
def weather():
    # Fetch weather data from OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return jsonify({
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'city': CITY
        })
    else:
        return jsonify({'error': 'Unable to fetch weather data'}), 500

@app.route('/api/time')
def time():
    # Get current time and date
    now = datetime.datetime.now()
    return jsonify({
        'time': now.strftime('%H:%M:%S'),
        'date': now.strftime('%Y-%m-%d')
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

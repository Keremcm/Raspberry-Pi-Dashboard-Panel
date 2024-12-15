# Raspberry Pi Dashboard

This is a Flask-based web application that provides a real-time dashboard for monitoring system information, weather data, and time/date on a Raspberry Pi. It is designed to be lightweight and visually appealing, making it an excellent addition to your Raspberry Pi projects.

## Features

- **System Monitoring**: Displays CPU usage, RAM usage, disk usage, and CPU temperature.
- **Weather Information**: Fetches real-time weather data using the OpenWeatherMap API.
- **Time and Date**: Shows the current time and date in a user-friendly format.
- **Dynamic Charts**: Uses Chart.js to render real-time line charts for system metrics.
- **Mobile-Friendly UI**: Designed with Bootstrap for responsiveness.

## Prerequisites

- Raspberry Pi (or any Linux-based system with Python installed)
- Python 3.11+
- Pip (Python package manager)

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/raspberry-pi-dashboard.git
   cd raspberry-pi-dashboard
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Environment Variables**
   Replace `API_KEY` and `CITY` in the `app.py` file with your OpenWeatherMap API key and desired city.

   ```python
   API_KEY = "your_api_key_here"
   CITY = "Your_City"
   ```

4. **Run the Application**
   ```bash
   python app.py
   ```

5. **Access the Dashboard**
   Open a web browser and navigate to `http://<raspberry-pi-ip>:5000/`.

## API Endpoints

The application exposes the following API endpoints:

### `/api/system_info`
Returns system metrics like CPU usage, RAM usage, disk usage, and CPU temperature.

**Example Response**:
```json
{
    "cpu_usage": 35.2,
    "ram_usage": 58.7,
    "disk_usage": 70.1,
    "temperature": 45.3
}
```

### `/api/weather`
Fetches real-time weather information.

**Example Response**:
```json
{
    "temperature": 15.3,
    "description": "clear sky",
    "city": "Bursa, Mudanya"
}
```

### `/api/time`
Provides the current time and date.

**Example Response**:
```json
{
    "time": "14:35:22",
    "date": "2024-12-15"
}
```

## Frontend

The frontend is built using Bootstrap and Chart.js for a modern and responsive user experience. It includes:

- **System Status Cards**: Real-time graphs for CPU, RAM, and disk usage.
- **Weather Information**: Displays current temperature and weather conditions.
- **Time and Date**: Shows current time and date in a card layout.

## Customization

- **Weather API**: Update the `API_KEY` and `CITY` variables in `app.py` for personalized weather data.
- **Styles**: Modify the `style` section in `index.html` to customize the appearance.
- **Data Refresh Rates**: Update the JavaScript intervals in `index.html` to control refresh frequency.

## Dependencies

- Flask
- psutil
- requests
- Chart.js
- Bootstrap

Install dependencies using:
```bash
pip install flask psutil requests
```

## Screenshots

### System Metrics
![System Metrics](https://via.placeholder.com/600x300)

### Weather Information
![Weather Info](https://via.placeholder.com/600x300)

### Time and Date
![Time and Date](https://via.placeholder.com/600x300)

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute as needed.

## Contribution

Contributions are welcome! Feel free to submit pull requests or open issues for suggestions and improvements.

---

Enjoy using the Raspberry Pi Dashboard!

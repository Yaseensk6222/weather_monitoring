from flask import Flask, render_template, request, session, redirect, url_for
import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key for session security
API_KEY = '242557d9b5f740f54089c4664fd49993'
BASE_URL = 'https://api.openweathermap.org/data/2.5/'

def convert_temperature(temp, scale):
    """Convert temperature from Kelvin to the preferred scale."""
    if scale == 'Celsius':
        return temp - 273.15
    elif scale == 'Fahrenheit':
        return (temp - 273.15) * 9/5 + 32
    elif scale == 'Kelvin':
        return temp
    return temp

def fetch_weather_data(city):
    """Fetch current weather data for a given city."""
    url = f"{BASE_URL}weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    return response.json()

def fetch_forecast_data(city):
    """Fetch 5-day weather forecast data for a given city."""
    url = f"{BASE_URL}forecast?q={city}&appid={API_KEY}"
    response = requests.get(url)
    return response.json()

def fetch_multiple_cities_weather_data(cities):
    """Fetch weather data for multiple cities."""
    weather_data = {}
    for city in cities:
        data = fetch_weather_data(city)
        if data.get('cod') != '404':
            weather_data[city] = data
    return weather_data

@app.route('/', methods=['GET', 'POST'])
def index():
    """Render the index page with current weather data."""
    if request.method == 'POST':
        city = request.form['city']
        weather_data = fetch_weather_data(city)
        if weather_data.get('cod') != '404':
            return render_template('index.html', weather=weather_data, convert_temperature=convert_temperature)
        else:
            error_message = "City not found. Please try again."
            return render_template('index.html', error=error_message)
    return render_template('index.html')

@app.route('/forecast', methods=['GET', 'POST'])
def forecast():
    """Render the forecast page with weather forecast data."""
    if request.method == 'POST':
        city = request.form['city']
        forecast_data = fetch_forecast_data(city)
        if forecast_data.get('cod') != '404':
            daily_data = {}
            for item in forecast_data['list']:
                date_str = item['dt_txt'].split(" ")[0]
                if date_str not in daily_data:
                    daily_data[date_str] = {
                        'temperatures': [],
                        'humidity': [],
                        'wind_speed': [],
                        'condition': item['weather'][0]['description']
                    }
                daily_data[date_str]['temperatures'].append(item['main']['temp'])
                daily_data[date_str]['humidity'].append(item['main']['humidity'])
                daily_data[date_str]['wind_speed'].append(item['wind']['speed'])

            forecast_summary = []
            for date, data in daily_data.items():
                avg_temp = sum(data['temperatures']) / len(data['temperatures'])
                max_temp = max(data['temperatures'])
                min_temp = min(data['temperatures'])
                forecast_summary.append({
                    'date': date,
                    'avg_temp': avg_temp,
                    'max_temp': max_temp,
                    'min_temp': min_temp,
                    'condition': data['condition'],
                    'humidity': sum(data['humidity']) // len(data['humidity']),
                    'wind_speed': sum(data['wind_speed']) / len(data['wind_speed'])
                })
            return render_template('forecast.html', forecast_data=forecast_summary, city=city, convert_temperature=convert_temperature)
        else:
            error_message = "City not found. Please try again."
            return render_template('forecast.html', error=error_message, forecast_data=[])
    return render_template('forecast.html', forecast_data=[])

@app.route('/metro_cities', methods=['GET'])
def metro_cities():
    """Render the metro cities page with weather data for Indian metro cities."""
    cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
    weather_data = fetch_multiple_cities_weather_data(cities)

    metro_data = {}
    for city, data in weather_data.items():
        metro_data[city] = {
            'avg_temp': convert_temperature(data['main']['temp'], session.get('preferred_scale', 'Celsius')),
            'condition': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }

    return render_template('metro_cities.html', metro_data=metro_data, convert_temperature=convert_temperature)

@app.route('/preferences', methods=['GET', 'POST'])
def preferences():
    """Render the preferences page to set temperature scale."""
    if request.method == 'POST':
        preferred_scale = request.form.get('preferred_scale', 'Celsius')
        session['preferred_scale'] = preferred_scale
        return redirect(url_for('preferences'))
    return render_template('preferences.html', preferred_scale=session.get('preferred_scale', 'Celsius'))

@app.route('/thresholds', methods=['GET', 'POST'])
def thresholds():
    alerts = []
    weather = {}  # Initialize weather to avoid undefined error
    if request.method == 'POST':
        city = request.form['city']
        threshold_temp = float(request.form['threshold_temp'])
        threshold_condition = request.form['threshold_condition']
        weather = fetch_weather_data(city)  # Change this to fetch_weather_data

        if weather and weather.get('cod') != '404':
            current_temp = convert_temperature(weather['main']['temp'], session.get('preferred_scale', 'Celsius'))
            current_condition = weather['weather'][0]['main']

            # Check thresholds
            if current_temp > threshold_temp:
                alerts.append(f"Alert: Temperature in {city} exceeds the threshold! (Current: {current_temp}°C)")
            if current_condition.lower() == threshold_condition.lower():
                alerts.append(f"Alert: Weather condition in {city} matches the threshold!")

        else:
            return render_template('thresholds.html', error="City not found.", convert_temperature=convert_temperature)

    return render_template('thresholds.html', weather=weather, alerts=alerts, convert_temperature=convert_temperature)

if __name__ == '__main__':
    app.run(debug=True)

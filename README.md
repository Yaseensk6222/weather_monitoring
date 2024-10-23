Weather Monitoring Application
This project is a Flask-based web application that allows users to monitor real-time weather data for various cities, set temperature thresholds, and configure alerts based on weather conditions using the OpenWeatherMap API. The application also provides options to view the 5-day weather forecast for metro cities in India.
Features
Real-time Weather Data: Fetches current weather information for any city.
Temperature Conversion: Users can set temperature preferences in Celsius, Fahrenheit, or Kelvin.
Weather Thresholds: Allows users to set thresholds for temperature and weather conditions and triggers alerts when thresholds are breached.
5-Day Forecast: Retrieves the 5-day weather forecast for key metro cities in India (Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad).
Preferences Page: Users can configure temperature units.
Real-Time Metro City Data: Displays real-time weather conditions for metro cities.
Alerts: Custom alerts when the weather exceeds user-defined thresholds.
Technologies Used
Python (Flask Framework)
HTML5/CSS3 (Bootstrap 4.5 for responsive design)
JavaScript (for front-end interactivity)
OpenWeatherMap API (for weather data)
PostgreSQL (or SQLite if you want a local lightweight database)
Jinja2 Templating (for dynamic HTML generation in Flask)
Installation
1. Clone the repository
bash
Copy code
git clone https://github.com/your-username/weather-monitoring-app.git
cd weather-monitoring-app
2. Set up a virtual environment
bash
Copy code
python -m venv venv
3. Activate the virtual environment
On Windows:
bash
Copy code
venv\Scripts\activate
On macOS/Linux:
bash
Copy code
source venv/bin/activate
4. Install dependencies
bash
Copy code
pip install -r requirements.txt
5. Set up environment variables
Create a .env file in the project root directory and add your OpenWeatherMap API key:

env
Copy code
OPENWEATHER_API_KEY=your-api-key-here
6. Run the application
bash
Copy code
python app.py
7. Access the app
Open your browser and go to http://127.0.0.1:5000/.

Usage
Home Page: Enter a city to retrieve the current weather conditions.
Preferences: Set your temperature unit (Celsius, Fahrenheit, or Kelvin).
Thresholds: Configure temperature and weather condition thresholds, and simulate alerts when conditions are breached.
Metro Cities Weather: View real-time weather data for metro cities in India.
5-Day Forecast: Get the 5-day weather forecast for the selected cities.




weather-monitoring-app/
│
├── app.py                   # Main application logic
├── requirements.txt          # Python dependencies
├── .env                      # API keys (not included in the repo)
├── templates/
│   ├── index.html            # Home page template
│   ├── preferences.html       # Preferences page template
│   ├── thresholds.html       # Thresholds configuration page
│   ├── metro_cities.html     # Real-time weather for metro cities
├── static/                   # Static files (e.g., CSS, JS)
│   └── css/
│       └── style.css         # Custom styles
├── README.md                 # Project documentation
├── .gitignore                # Files to ignore in Git



Future Enhancements
Historical Data: Display weather trends using historical data.
Additional Cities: Allow users to select cities outside of the current metros.
User Authentication: Enable users to create accounts and save preferences permanently.
Push Notifications: Implement email or SMS alerts when weather thresholds are breached.

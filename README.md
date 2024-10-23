Detailed Instructions to Run the Weather Monitoring Application
Prerequisites:
Before running the application, make sure you have the following installed:
1.	Python 3.x: You can download Python here. Ensure Python is added to your system's PATH during installation.
o	Verify installation:
bash
Copy code
python --version
2.	pip: This should be installed automatically with Python. To verify:
bash
Copy code
pip --version
3.	PostgreSQL (Optional): If you're using PostgreSQL as your database. You can install it here.
4.	Virtual Environment (Recommended): It's a good practice to create a virtual environment for Python projects to avoid conflicts between dependencies.
________________________________________
Step-by-Step Guide to Run the Project:
1. Clone the GitHub Repository
First, you need to clone the repository to your local machine:
bash
Copy code
git clone https://github.com/your-username/weather-monitoring-app.git
cd weather-monitoring-app
2. Set Up a Virtual Environment
•	Create the virtual environment:
bash
Copy code
python -m venv venv
•	Activate the virtual environment:
o	On Windows:
bash
Copy code
venv\Scripts\activate
o	On macOS/Linux:
bash
Copy code
source venv/bin/activate
3. Install Dependencies
After activating the virtual environment, install the required dependencies listed in requirements.txt:
bash
Copy code
pip install -r requirements.txt
The requirements.txt file will install the following packages:
•	Flask: To build the web server and handle routes.
•	Requests: To make HTTP requests to the OpenWeatherMap API.
•	psycopg2-binary: To interact with the PostgreSQL database (if you use PostgreSQL).
•	python-dotenv: For loading environment variables from a .env file.
4. Obtain an API Key from OpenWeatherMap
You need an API key from OpenWeatherMap to fetch weather data. Follow these steps:
1.	Go to OpenWeatherMap and sign up.
2.	Once logged in, go to the API keys section and generate a new key.
3.	Copy the key.
5. Set Up Environment Variables
In the root folder of the project, create a .env file and add the following lines:
bash
Copy code
OPENWEATHER_API_KEY=your-api-key-here
DATABASE_URL=postgresql://postgres:your_password@localhost/weatherdb  # If using PostgreSQL
Replace your-api-key-here with the actual OpenWeatherMap API key and set the correct database URL.
6. Initialize the Database (Optional for PostgreSQL)
If you're using PostgreSQL as your database, ensure the database is set up. You can create the database like this:
1.	Log into PostgreSQL:
bash
Copy code
psql -U postgres
2.	Create the database:
sql
Copy code
CREATE DATABASE weatherdb;
3.	Update the DATABASE_URL in .env accordingly.
If you prefer using SQLite (which is simpler for testing), Flask will automatically create the weather.db file when you first run the app. You don't need additional configuration for this.
7. Run the Application
With everything set up, you can run the Flask application with the following command:
bash
Copy code
python app.py
This will start a local server at http://127.0.0.1:5000/.
8. Access the Application
Open your browser and navigate to http://127.0.0.1:5000/. You should now be able to use the weather monitoring application.
________________________________________
Project Files Overview for GitHub
When uploading the project to GitHub, make sure to include the following:
1.	app.py: The main Flask application file, handling routes and weather data processing.
2.	requirements.txt: A list of dependencies required to run the project.
To generate requirements.txt (if not already included):
bash
Copy code
pip freeze > requirements.txt
3.	templates/: Contains the HTML templates (e.g., index.html, metro_cities.html, preferences.html, thresholds.html).
4.	static/: Any static files such as CSS (e.g., style.css), JavaScript, or images.
5.	.env.example: An example .env file for reference. Do not include your actual .env file (with API keys) in the repository.
Example:
bash
Copy code
OPENWEATHER_API_KEY=your-api-key-here
DATABASE_URL=postgresql://postgres:your_password@localhost/weatherdb
6.	README.md: A detailed README file explaining how to set up and run the project (like the one we've prepared).
7.	.gitignore: Ensure you have a .gitignore file to prevent sensitive files (like .env) and unnecessary files (e.g., virtual environments, .pyc files) from being uploaded.
Example .gitignore:
bash
Copy code
__pycache__/
*.pyc
venv/
.env
.DS_Store
8.	weather.db: If you're using SQLite for your database, you may want to include this as a sample database file.
9.	LICENSE: Add a license file to specify how others can use your code. If you're unsure, you can use the MIT license, which is commonly used for open-source projects.
________________________________________
Testing
Once the project is set up, ensure it is working by testing the following:
1.	Enter a city on the homepage and retrieve weather data.
2.	Change temperature preferences (Celsius, Fahrenheit, Kelvin) on the preferences page.
3.	Set temperature and condition thresholds, simulate a weather breach, and check if alerts trigger correctly.
4.	View weather for metro cities in India and check for real-time updates.


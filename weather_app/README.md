# Weather Data Center 🌤️

A simple Python command-line app to fetch current weather or weekly forecast data using the OpenWeatherMap API.

---

## Features

- Get today's weather for any city
- Get weekly weather forecast for a specified city, state, and country
- Displays temperature in Fahrenheit (imperial units)

---

## How to Use

1. **Set up your OpenWeatherMap API key:**

Create a `.env` file in the project directory containing:

API_KEY=your_openweathermap_api_key_here


2. **Install dependencies:**

```bash
pip install requests python-dotenv

3. Run the app:

python weather_app.py

4. Follow the prompts:

Choose today for current weather by city name.

Choose week for a weekly forecast (requires city, state, country inputs).

Requirements
Python 3.x

requests library

python-dotenv for environment variable management
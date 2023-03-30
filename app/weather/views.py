import os
import requests
from flask import render_template, request
from . import weather

API_KEY = os.environ.get('WEATHER_API_KEY') 

def get_weather_data(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    return response.json()

@weather.route('/weather', methods=['GET', 'POST'])
def weather_page():
    city = None
    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather_data(city)
        return render_template('weather/weather.html', city=city, weather_data=weather_data)
    return render_template('weather/weather.html')

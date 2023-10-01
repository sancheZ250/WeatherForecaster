from django.shortcuts import render
import requests

def index(request):
    if request.method == 'POST':
        api_key = '8c3431052deac27e1e526388cfd1769d'
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"

        response = requests.get(api_url)

        if response.status_code == 200:
            weather_data = response.json()
            name = weather_data['name']
            temperature = weather_data['main']['temp']
            feels_like = weather_data['main']['feels_like']
            weather_condition = weather_data['weather'][0]['description']
            wind_speed = weather_data['wind']['speed']
            humidity = weather_data['main']['humidity']
            pressure = weather_data['main']['pressure']

            context = {
                'temperature': temperature,
                'weather_condition': weather_condition,
                'wind_speed': wind_speed,
                'humidity': humidity,
                'pressure': pressure,
                'feels_like': feels_like,
                'name': name,
            }

            return render(request, 'Weather/index.html', context=context)

        else:
            error_message = "Error fetching weather data"
            return render(request, 'Weather/index.html', {'error_message': error_message})

    return render(request, 'Weather/index.html')
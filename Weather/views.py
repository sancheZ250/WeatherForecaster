from django.shortcuts import render
import requests

def index(request):
    if request.method == 'POST':
        api_id = '8c3431052deac27e1e526388cfd1769d'
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_id}&units='standart'"

        response = requests.get(api_url)

        if response.status_code == 200:
            weather_data = response.json()
            temperature = round(weather_data['main']['temp']-272.1)
            weather_condition = weather_data['weather'][0]['description']
            wind_speed = weather_data['wind']['speed']

            context = {
                'temperature': temperature,
                'weather_condition': weather_condition,
                'wind_speed': wind_speed
            }

            return render(request, 'Weather/index.html', context=context)

        else:
            error_message = "Error fetching weather data"
            return render(request, 'Weather/index.html', {'error_message': error_message})

    return render(request, 'Weather/index.html')

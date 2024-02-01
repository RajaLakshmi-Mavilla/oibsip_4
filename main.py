import requests

def get_weather(api_key, city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {'q': city, 'units': 'metric', 'APPID': api_key}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Check for HTTP errors
        weather_data = response.json()

        if weather_data['cod'] == 200:
            return weather_data
        else:
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def display_weather(weather_data):
    if not weather_data:
        print("No City Found or Error fetching data.")
    else:
        weather = weather_data['weather'][0]['main']
        temp = round(weather_data['main']['temp'])

        print(f"The weather is: {weather}")
        print(f"The temperature is: {temp}°C")

def main():
    api_key = '30d4741c779ba94c470ca1f63045390a'
    user_input = input("Enter city: ")

    weather_data = get_weather(api_key, user_input)
    display_weather(weather_data)

# Run the main function
main()
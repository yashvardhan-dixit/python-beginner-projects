import requests

API_KEY = "45a61531ac5b8fb7d36a5132a62bd8d7"  # 🔑 Replace with your working key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code == 200:
            print(f"\n🌤️ Weather in {data['name']}, {data['sys']['country']}")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Humidity: {data['main']['humidity']}%")
            print(f"Weather: {data['weather'][0]['description'].capitalize()}")
        else:
            print(f"❌ Error {response.status_code}: {data.get('message', 'City not found or request failed')}")
    except Exception as e:
        print("⚠️ Something went wrong:", e)

while True:
    city = input("\n🏙️ Enter city name (or type 'exit' to quit): ")
    if city.lower() == 'exit':
        print("👋 Bye! Stay weather-wise!")
        break
    get_weather(city)

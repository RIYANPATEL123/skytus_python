import requests
from config import API_KEY

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Celsius
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()

        name        = data["name"]
        country     = data["sys"]["country"]
        temp        = data["main"]["temp"]
        feels_like  = data["main"]["feels_like"]
        temp_min    = data["main"]["temp_min"]
        temp_max    = data["main"]["temp_max"]
        humidity    = data["main"]["humidity"]
        wind_speed  = data["wind"]["speed"]
        condition   = data["weather"][0]["description"].title()

        print(f"""

    {name}, {country}
    Condition  : {condition}
    Temp       : {temp}°C (Feels like {feels_like}°C)
    Max        : {temp_max}°C
    Min        : {temp_min}°C
    Humidity   : {humidity}%
    Wind Speed : {wind_speed} m/s
  
        """)

    elif response.status_code == 404:
        print("\n   City not found. Please check the name and try again.")
    elif response.status_code == 401:
        print("\n   Invalid API key. Please check config.py.")
    else:
        print(f"\n   Error: {response.status_code}. Something went wrong.")

def main():
    
    print(" WEATHER APP  ")
   
    while True:
        city = input("\n  Enter city name (or 'exit' to quit): ").strip()

        if city.lower() == "exit":
            print("\nGoodbye!\n")
            break
        elif city == "":
            print("Please enter a city name.")
        else:
            get_weather(city)

if __name__ == "__main__":
    main()
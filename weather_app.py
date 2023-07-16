import requests
import json

def get_weather_data(city):
    api_key = "e78e53bd7dfcd2ff6ab48fb26e811769"
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(api_url, params={"q": city})
    data = response.json()
    return data

def display_weather_data(data):
    if "error" in data:
        print("Error:", data["error"]["message"])
    else:
        temperature = data["main"]["temp"]
        temperature_celsius = temperature - 273.15
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        pressure = data["main"]["pressure"]
        visibility = data["visibility"] if "visibility" in data else "N/A"

        print("\n------ WEATHER INFORMATION ------\n")
        print(f"TEMPERATURE:  {temperature_celsius:.2f} °C")
        print(f"HUMIDITY:     {humidity}%")
        print(f"WIND SPEED:   {wind_speed} m/s")
        print(f"PRESSURE:     {pressure} hPa")
        print(f"VISIBILITY:   {visibility} meters")

def main():
    city = input("Enter a city: ")
    data = get_weather_data(city)
    display_weather_data(data)

if __name__ == "__main__":
    main()























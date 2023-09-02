import pip._vendor.requests
import json

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    response = pip._vendor.requests.get(complete_url)
    data = response.json()
    
    if data["cod"] != "404":
        weather_info = {
            "City": data["name"],
            "Temperature (°C)": data["main"]["temp"],
            "Weather": data["weather"][0]["description"],
            "Humidity (%)": data["main"]["humidity"],
            "Wind Speed (m/s)": data["wind"]["speed"],
        }
        return weather_info
    else:
        return None

def main():
    api_key = "Enter Api Key"
    city = input("Enter city name: ")

    weather_data = get_weather(api_key, city)

    if weather_data:
        print("\nWeather Information for", weather_data["City"])
        for key, value in weather_data.items():
            print(f"{key}: {value}")
    else:
        print("City not found. Please check the spelling or try another city.")

if __name__ == "__main__":
    main()
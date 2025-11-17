import requests

API_KEY = "YOUR_API_KEY_GOES_HERE" 
CITY = "New York"
UNITS = "metric"

def get_weather(city, api_key, units):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}"
    print(f"Fetching weather for {city}...")
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        desc = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        unit_sym = "C" if units == "metric" else "F"
        
        print(f"Weather: {desc.capitalize()}")
        print(f"Temp: {temp} {unit_sym}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_weather(CITY, API_KEY, UNITS)

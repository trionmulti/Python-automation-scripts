import requests
import sys

# --- CONFIGURATION ---

# 1. Paste your OpenWeatherMap API key here.
API_KEY = "YOUR_API_KEY_GOES_HERE" 

# 2. The city you want the weather for.
CITY = "New York"

# 3. Units for temperature:
#    'metric' for Celsius, 'imperial' for Fahrenheit
UNITS = "metric"
# ---------------------


def get_weather(city, api_key, units):
    """
    Fetches and displays the current weather for a given city.
    """
    
    # 1. Build the API URL
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    # "q=" for city, "appid=" for key, "units=" for C/F
    url = f"{base_url}?q={city}&appid={api_key}&units={units}"
    
    print(f"Fetching weather for {city}...\n")
    
    try:
        # 2. Make the API request
        response = requests.get(url)
        
        # Raise an exception for bad status codes (like 404, 500)
        response.raise_for_status()
        
        # 3. Parse the JSON data
        #    This converts the text response into a Python dictionary
        data = response.json()
        
        # 4. Extract the useful information
        #    (You can print(data) to see all the info available!)
        city_name = data["name"]
        country = data["sys"]["country"]
        description = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        
        # Determine the unit symbol
        unit_symbol = "°C" if units == "metric" else "°F"
        
        # 5. Display the formatted weather report
        print("--- Current Weather Report ---")
        print(f" Location: {city_name}, {country}")
        print(f" Condition: {description.capitalize()}")
        print(f" Temperature: {temp}{unit_symbol}")
        print(f" Feels Like: {feels_like}{unit_symbol}")
        print("--------------------------------")

    except requests.exceptions.HTTPError as e:
        # Handle specific HTTP errors (like 401 Unauthorized or 404 Not Found)
        if e.response.status_code == 401:
            print("Error: Authentication failed. Check your API_KEY.")
        elif e.response.status_code == 404:
            print(f"Error: City not found. Check the spelling of '{city}'.")
        else:
            print(f"An HTTP error occurred: {e}")
    except requests.exceptions.RequestException as e:
        # Handle other network issues (e.g., no internet connection)
        print(f"A network error occurred: {e}")
    except KeyError:
        # Handle cases where the JSON response is missing expected data
        print("Error: Could not parse weather data. The API response may have changed.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if API_KEY == "YOUR_API_KEY_GOES_HERE":
        print("Error: Please set your API_KEY in the script configuration.")
    else:
        get_weather(CITY, API_KEY, UNITS)

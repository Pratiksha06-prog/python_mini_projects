#WEATHER APP FOR BEGINNERS
import requests
#step1: take a input for city
city = input("Enter the city name:")

#step2: add your API key from openweather
api_key = "82be9028b619cb3f5b74669031671314"
url = url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

#step3: check if request was successfully or not
if response.status_code == 200:
    data = response.json()

#step4: extract required info
    temperature = data['main']['temp']
    humidity = data['main']['humidity'] 
    condition = data['weather'][0]['description']

#step8: print the results
    print(f"\nWeather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {condition.capitalize()}")
else:
    print("Error: City not found. Please try again.")
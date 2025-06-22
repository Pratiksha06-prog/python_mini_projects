#ADVANCED WEATHER APP
import requests
import tkinter as tk
from tkinter import messagebox

# Function to get weather
def get_weather():
    city = city_entry.get()
    api_key = "82be9028b619cb3f5b74669031671314"  

    if city == "":
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temp_c = data['main']['temp']
            temp_f = temp_c * 9/5 + 32
            humidity = data['main']['humidity']
            wind = data['wind']['speed']
            desc = data['weather'][0]['description'].capitalize()

            result = (
                f"Weather in {city}:\n"
                f"Condition: {desc}\n"
                f"Temperature: {temp_c}°C / {temp_f:.1f}°F\n"
                f"Humidity: {humidity}%\n"
                f"Wind Speed: {wind} m/s"
            )
            output_label.config(text=result)
        else:
            output_label.config(text="City not found. Please try again.")
    except:
        output_label.config(text="Something went wrong. Please check your internet or API key.")

# GUI Setup
root = tk.Tk()
root.title("Advanced Weather App")
root.geometry("400x300")
root.config(bg="#e6f2ff")

# Widgets
tk.Label(root, text="Enter City Name:", bg="#e6f2ff", font=("Aerial", 12)).pack(pady=10)
city_entry = tk.Entry(root, width=30, font=("Arial", 12))
city_entry.pack()

tk.Button(root, text="Get Weather", command=get_weather, bg="#4da6ff", font=("Arial", 12)).pack(pady=10)

output_label = tk.Label(root, text="", bg="#e6f2ff", font=("Arial", 12), justify="left")
output_label.pack(pady=10)

root.mainloop()

import tkinter as tk
import requests
import time
import os
import platform
import ctypes

if platform.system() == "Windows":
    current_directory = os.path.dirname(os.path.abspath(__file__))

    def getWeather(canvas):
        city = textField.get()
        api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=793fbe99a4b8fe92defaece269192aaf"
    
# Get JSON data from API
        json_data = requests.get(api).json()

# Check for valid city

        if json_data['cod'] != 200:
            label1.config(text="City not found")
        else:
    # Extract relevant information from JSON data
            condition = json_data['weather'][0]['main']
            temp = int(json_data['main']['temp'] - 273.15)
            min_temp = int(json_data['main']['temp_min'] - 273.15)
            max_temp = int(json_data['main']['temp_max'] - 273.15)
            pressure = json_data['main']['pressure']
            humidity = json_data['main']['humidity']
            wind = json_data['wind']['speed']
            sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
            sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))
    
    # Create final strings for display
        final_info = f"{condition}\n{temp}°C"
        final_data = (f"\nMin Temp: {min_temp}°C\nMax Temp: {max_temp}°C\nPressure: {pressure}\n"
                  f"Humidity: {humidity}\nWind Speed: {wind}\nSunrise: {sunrise}\nSunset: {sunset}")
    
    # Update labels with final information
        label1.config(text=final_info)
        label2.config(text=final_data)


# Set the wallpaper based on the weather condition
        if condition == "Clear":
            wallpaper_path = os.path.join(current_directory, "wallpapers", "clear_wallpaper.jpg")
            ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_path, 0)
        elif condition == "Clouds":
            wallpaper_path = os.path.join(current_directory, "wallpapers", "clouds_wallpaper.jpg")
            ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_path, 0)
        elif condition == "Haze":
            wallpaper_path = os.path.join(current_directory, "wallpapers", "haze_wallpaper.jpg")
            ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_path, 0)
        elif condition == "Mist":
            wallpaper_path = os.path.join(current_directory, "wallpapers", "mist_wallpaper.jpg")
            ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_path, 0)
        elif condition == "Rain":
            wallpaper_path = os.path.join(current_directory, "wallpapers", "rain_wallpaper.jpg")
            ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_path, 0)
        elif condition == "Smoke":
            wallpaper_path = os.path.join(current_directory, "wallpapers", "smoke_wallpaper.jpg")
            ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_path, 0)
        elif condition == "Snow":
            wallpaper_path = os.path.join(current_directory, "wallpapers", "snow_wallpaper.jpg")
            ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_path, 0)
        elif condition == "Sunny":
            wallpaper_path = os.path.join(current_directory, "wallpapers", "sunny_wallpaper.jpg")
            ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_path, 0)
        elif condition == "Fog":
            wallpaper_path = os.path.join(current_directory, "wallpapers", "fog_wallpaper.jpg")
            ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_path, 0)
        else:
            wallpaper_path = os.path.join(current_directory, "wallpapers", "normal_wallpaper.jpg")
            ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_path, 0)

else:
    def getWeather(canvas):
        city = textField.get()
        api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=793fbe99a4b8fe92defaece269192aaf"
    
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        temp = int(json_data['main']['temp'] - 273.15)
        min_temp = int(json_data['main']['temp_min'] - 273.15)
        max_temp = int(json_data['main']['temp_max'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
        sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))
        final_info = condition + "\n" + str(temp) + "°C" 
        final_data = "\n"+ "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
        label1.config(text = final_info)
        label2.config(text = final_data)

# Set the wallpaper based on the weather condition
        current_dir = os.getcwd()
        if condition == "Clear":
            wallpaper_path = os.path.join(current_dir, "wallpapers/clear_wallpaper.jpg")
            os.system("gsettings set org.gnome.desktop.background picture-uri file://" + wallpaper_path)
        elif condition == "Clouds":
            wallpaper_path = os.path.join(current_dir, "wallpapers/clouds_wallpaper.jpg")
            os.system("gsettings set org.gnome.desktop.background picture-uri file://" + wallpaper_path)
        elif condition == "Snow":
            wallpaper_path = os.path.join(current_dir, "wallpapers/snow_wallpaper.jpg")
            os.system("gsettings set org.gnome.desktop.background picture-uri file://" + wallpaper_path)
        elif condition == "Rain":
            wallpaper_path = os.path.join(current_dir, "wallpapers/rain_wallpaper.jpg")
            os.system("gsettings set org.gnome.desktop.background picture-uri file://" + wallpaper_path)
        elif condition == "Sunny":
            wallpaper_path = os.path.join(current_dir, "wallpapers/sunny_wallpaper.jpg")
            os.system("gsettings set org.gnome.desktop.background picture-uri file://" + wallpaper_path)
        elif condition == "Haze":
            wallpaper_path = os.path.join(current_dir, "wallpapers/haze_wallpaper.jpg")
            os.system("gsettings set org.gnome.desktop.background picture-uri file://" + wallpaper_path)
        elif condition == "Smoke":
            wallpaper_path = os.path.join(current_dir, "wallpapers/smoke_wallpaper.jpg")
            os.system("gsettings set org.gnome.desktop.background picture-uri file://" + wallpaper_path)
        elif condition == "Mist":
            wallpaper_path = os.path.join(current_dir, "wallpapers/mist_wallpaper.jpg")
            os.system("gsettings set org.gnome.desktop.background picture-uri file://" + wallpaper_path)
        elif condition == "Fog":
            wallpaper_path = os.path.join(current_dir, "wallpapers/fog_wallpaper.jpg")
            os.system("gsettings set org.gnome.desktop.background picture-uri file://" + wallpaper_path)
        else:
            wallpaper_path = os.path.join(current_dir, "wallpapers/normal_wallpaper.jpg")
            os.system("gsettings set org.gnome.desktop.background picture-uri file://" + wallpaper_path)

    canvas = tk.Tk()
    canvas.geometry("600x500")
    canvas.title("Weather App")
    f = ("poppins", 15, "bold")
    t = ("poppins", 35, "bold")

    textField = tk.Entry(canvas, justify='center', width = 20, font = t)
    textField.pack(pady = 20)
    textField.focus()
    textField.bind('<Return>', getWeather)

    label1 = tk.Label(canvas, font=t)
    label1.pack()
    label2 = tk.Label(canvas, font=f)
    label2.pack()
    canvas.mainloop()
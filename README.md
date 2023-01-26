# Weather App
This script is a weather app that uses the Tkinter library to create a GUI for the user to enter a city name and get the current weather conditions for that city. The weather data is obtained from the OpenWeatherMap API using the requests library. The script then displays the weather condition, temperature, minimum and maximum temperature, pressure, humidity, wind speed, sunrise, and sunset in a label on the GUI.

Additionally, it also changes the wallpaper of the desktop based on the current weather condition. It does this by calling the gsettings command to change the desktop background picture URI to the corresponding wallpaper file path. The script supports several different weather conditions such as "Clear", "Clouds", "Snow", "Rain", "Sunny", "Haze", "Smoke" and "Mist".

# Libraries Used
tkinter library
requests library
ctypes library
os library
time library
platform library

# To Run
python3 widget.py

# Data Sources
Weather information is retrieved from OpenWeatherMap using the Current Weather Data API. An API key is required, which can be obtained by creating a free account on the OpenWeatherMap website.

# Wallpaper Changing
The application changes the desktop wallpaper based on the current weather conditions. Wallpaper images are obtained from Unsplash.
The application has been tested on Ubuntu and Windows 10.

# Known Issues
Wallpaper changing feature is not compatible with MacOS
Application may not work properly with other desktop environments.

# Contribution
Feel free to fork the repository and submit pull requests for any bug fixes or new features.

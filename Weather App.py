from customtkinter import CTk, CTkFrame, CTkButton, CTkEntry, CTkLabel, CTkImage
import os
from datetime import datetime, timezone, timedelta
import pytz
from dotenv import load_dotenv
from geopy.geocoders import Nominatim
from PIL import Image, ImageTk
import requests

load_dotenv('API.env')
API_KEY = os.environ.get('API')

# color palette & fonts
lblue = "#39C0FA"
lwhite = "#f3f3f3"
white = "#FFFFFF"
black = "#000000"
trp = "transparent"
regfont = "Adobe Clean"
boldfont = "Adobe Clean UX"

path = 'Resources/assets/'
weather = 'Resources/assets/WeatherTypes/'
welcome_txt = "Welcome to our weather app! \nTo get started, simply type in the name of a city or town and discover the forecast for that area. \nWhether you're planning a trip or just curious about the weather in your area, our app has got you covered. \nSo go ahead, explore and discover the beauty of weather in different parts of the world. \nLet's get started!"

window = CTk(fg_color="#f3f3f3")
window.geometry("850x535")
window.resizable(False, False)
window.title("Weather")
window.iconbitmap(f'{path}ico.ico')


# Functions
def GetWeather():
    city = location.get()
    geolocator = Nominatim(user_agent="Weather_App")

    try:
        location_data = geolocator.geocode(city)
        latitude = location_data.latitude
        longitude = location_data.longitude
        
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}"
        response = requests.get(url, timeout=7)
        print(response.content)
        print(response.status_code)

        if response.status_code == 200:
            WeatherInfo = response.json()
            
            temperatureKelvin = WeatherInfo["main"]["temp"]
            humidity = WeatherInfo["main"]["humidity"]
            wind_speed = WeatherInfo["wind"]["speed"]
            pressure = WeatherInfo["main"]["pressure"]
            description = WeatherInfo["weather"][0]["description"]
            country = WeatherInfo["sys"]["country"]
            place = WeatherInfo["name"]
            time = WeatherInfo["timezone"]
            sunriseTime = WeatherInfo["sys"]["sunrise"]
            sunsetTime = WeatherInfo["sys"]["sunset"]
            
            # Neccessary Conversions
            temperature = round(temperatureKelvin-273)
            timezone = pytz.timezone('UTC')  # Start with UTC timezone
            current_time = datetime.now(timezone) + timedelta(seconds=time)
            sunrise = datetime.fromtimestamp(sunriseTime, tz=timezone)
            sunset = datetime.fromtimestamp(sunsetTime, tz=timezone)
            
            print(f'{current_time}\n\n{sunset}\n\n{sunrise}')
            
            # Update the weather information in the GUI
            if sunrise.time() < current_time.time() < sunset.time():
                currentmode_txt.configure(text="Sunrise")
            elif sunrise.time() > current_time.time():
                currentmode_txt.configure(text="Sunset")
            else:
                currentmode_txt.configure(text="No Data")
            
            text2.configure(text=f"{temperature}°")
            country_txt.configure(text=country)
            place_txt.configure(text=place)
            time_txt.configure(text=current_time.strftime("%H:%M:%S"))
            date_txt.configure(text=current_time.strftime("%d/%m/%Y"))
            
            DESCRIPTIONInfo.configure(text=description.capitalize())
            HUMIDITYInfo.configure(text=f"{humidity}%")
            WINDInfo.configure(text=f"{wind_speed} m/s")
            PRESSUREInfo.configure(text=f"{pressure} hPa")
            
            ldescription = description.lower()
            
            if ldescription in WeatherImages:
                weather_img.configure(image=WeatherImages[ldescription])
                
            if ldescription in WeatherDescriptions:
                text3.configure(text=WeatherDescriptions[ldescription], justify='left')
                
            else:
                weather_img.configure(image=Idefult)

        else:
            print("Failed to retrieve weather data.")

    except Exception as Error:
        # Display an error message with the real error, if an exception occurred
        print(f"An error occurred: {Error}")
        
def handle_enter(event):
    GetWeather()

#------------------------------Other Assets------------------------------
Isearch_btn = CTkImage(Image.open(f"{path}search_btn.png"), size=(32, 32))
Isearchbtn_hover = CTkImage(Image.open(f"{path}search_btn_hover.png"), size=(32, 32))
Irefresh_btn = CTkImage(Image.open(f"{path}refresh_btn.png"), size=(28, 28))
Irefreshbtn_hover = CTkImage(Image.open(f"{path}refresh_btn_hover.png"), size=(28, 28))


Idefult = CTkImage(Image.open(f"{path}defult.png"), size=(120, 120))
Idetailsbar = CTkImage(Image.open(f"{path}details_bar.png"), size=(850, 40))
Idetailsbartxt = CTkImage(Image.open(f"{path}detailsbar_txt.png"), size=(747, 14))
#------------------------------WEATHER TYPES------------------------------
sunny_img = CTkImage(Image.open(f"{weather}sunny.png"), size=(120, 120))
cloudy_img = CTkImage(Image.open(f"{weather}cloudy.png"), size=(120, 120))
rainy_img = CTkImage(Image.open(f"{weather}rainy.png"), size=(120, 120))
thunderstorm_img = CTkImage(Image.open(f"{weather}thunderstorm.png"), size=(120, 120))
snowy_img = CTkImage(Image.open(f"{weather}snowy.png"), size=(120, 120))
foggy_img = CTkImage(Image.open(f"{weather}foggy.png"), size=(120, 120))
tornado_img = CTkImage(Image.open(f"{weather}tornado.png"), size=(120, 120))
rainynight_img = CTkImage(Image.open(f"{weather}rainy_night.png"), size=(120, 120))
night_img = CTkImage(Image.open(f"{weather}night.png"), size=(120, 120))
cloudynight_img = CTkImage(Image.open(f"{weather}cloudy_night.png"), size=(120, 120))

# Weather Images
WeatherImages = {
    "clear sky": sunny_img,
    "few clouds": cloudy_img,
    "scattered clouds": cloudy_img,
    "broken clouds": cloudy_img,
    "overcast clouds": cloudy_img,
    "light rain": rainy_img,
    "moderate rain": rainy_img,
    "heavy rain": rainy_img,
    "thunderstorm": thunderstorm_img,
    "snow": snowy_img,
    "mist": foggy_img,
    "fog": foggy_img,
    "haze": foggy_img,
    "tornado": tornado_img,
    "light intensity shower rain": rainynight_img,
    "light intensity drizzle": rainynight_img,
    "night": night_img,
    "partly cloudy": cloudynight_img,
    "smoke": foggy_img
}
# Weather Descriptions
WeatherDescriptions = {
    "clear sky": "A clear sky indicates a lack of cloud cover, allowing ample sunlight to reach the surface. \nIt often accompanies pleasant weather conditions with bright sunshine and blue skies. \nPeople can enjoy outdoor activities and may need sun protection.",
    "few clouds": "Few clouds in the sky indicate a partially cloudy weather condition. \nIt combines periods of sunshine with some cloud cover. \nThe temperature might be moderate, and outdoor activities can be enjoyed with a mix of sun and clouds.",
    "scattered clouds": "Scattered clouds refer to a weather condition where clouds are spread out across the sky. \nIt can create a partly sunny and partly cloudy atmosphere. \nThe temperature might be comfortable, and outdoor activities can be enjoyed with variations in sunlight.",
    "broken clouds": "Broken clouds indicate a weather condition with a significant amount of cloud cover. \nThe clouds are not continuous but have gaps between them. \nIt can create a slightly gloomy atmosphere with limited sunshine. \nOutdoor activities might be less affected by direct sunlight but may require appropriate clothing.",
    "overcast clouds": "Overcast clouds refer to a weather condition with complete cloud cover, blocking out direct sunlight. \nIt can create a gray and dull atmosphere with no or minimal sunshine. \nThe temperature might be cooler than usual, and outdoor activities may be limited.",
    "light rain": "Light rain refers to a gentle and light precipitation of raindrops. \nIt can create a damp environment and wet surfaces. \nIt's advisable to carry an umbrella or wear a raincoat when venturing outdoors.",
    "moderate rain": "Moderate rain indicates a steady and moderate amount of rainfall. \nIt can result in wet conditions, puddles, and reduced visibility. \nIt's recommended to use proper rain gear and exercise caution while traveling or engaging in outdoor activities.",
    "heavy rain": "Heavy rain refers to intense and heavy precipitation with a high volume of rainfall. \nIt can lead to waterlogging, flooding, and hazardous conditions. \nIt's important to stay indoors, follow safety guidelines, and avoid areas prone to flooding.",
    "thunderstorm": "A thunderstorm is a weather condition characterized by thunder, lightning, and heavy rainfall. \nIt can also involve strong winds and occasionally hail. \nIt's essential to seek shelter indoors, stay away from tall objects, and follow thunderstorm safety precautions.",
    "snow": "Snowy weather occurs when precipitation falls as snowflakes and accumulates on the ground. \nIt creates a winter wonderland with a white blanket of snow. \nSnowy conditions may require warm clothing, boots, and caution while walking or driving on slippery surfaces.",
    "mist": "Mist refers to a weather condition with a thin, cloud-like layer close to the ground. \nIt can reduce visibility but is not as dense as fog. \nIn misty conditions, it's important to drive with caution and be aware of limited visibility in outdoor environments.",
    "fog": "Foggy weather results from the presence of dense fog, reducing visibility. \nIt occurs when moisture in the air condenses near the ground. \nIn foggy conditions, it's important to use fog lights while driving, move cautiously, and be aware of limited visibility in outdoor environments.",
    "haze": "Haze refers to a weather condition with reduced visibility and a fine suspension of dust, smoke, or pollutants in the air. \nIt can create a hazy or smoky atmosphere. \nPeople with respiratory issues may need to take precautions and limit outdoor activities.",
    "tornado": "A tornado is a violent and destructive weather phenomenon characterized by a rapidly rotating column of air. \nIt can cause significant damage to structures and pose a threat to life and safety. \nDuring a tornado, it is crucial to follow tornado safety"
}

#----------------------------------------------------------------------
navbar = CTkFrame(window, fg_color=lwhite, bg_color=trp, width=850, height=40)
searchbar = CTkFrame(window, fg_color=white, bg_color=white, width=300, height=40)
location = CTkEntry(window, text_color=black, placeholder_text="Search for location", placeholder_text_color=black, font=(regfont, 18), fg_color=white, bg_color=white, border_color=white, width=255, height=40)
detailsbar = CTkLabel(window, text='', image=Idetailsbar)
detailsbar_txt = CTkLabel(window, text='', image=Idetailsbartxt)
weather_img = CTkLabel(window, text='', image=Idefult, fg_color=trp)
bluebar = CTkFrame(window, fg_color=lblue, bg_color=lwhite, width=700, height=100, corner_radius=20)

# Buttons
searchbtn = CTkButton(window, text='', image=Isearch_btn, fg_color=white, bg_color=white, command=GetWeather,hover_color=lblue, corner_radius=0, width=32, height=32)
refreshbtn = CTkButton(window, text='', image=Irefresh_btn, fg_color=white, bg_color=white, command=GetWeather,hover_color="#d9d9d9", corner_radius=0, width=32, height=32)

# TEXTS
# I also added bg_color because in some cases GUI glitch and shows white lines around widgets
text1 = CTkLabel(window, text="Current Weather", fg_color=lwhite, font=(boldfont, 30, 'bold'), width=20)
text2 = CTkLabel(window, text="??°", text_color="#FF5151", fg_color=trp, font=(boldfont, 70), width=150)
text3 = CTkLabel(window, text=welcome_txt, text_color="#252525", fg_color=trp, font=(boldfont, 20), wraplength=500, anchor='w', width=500)

country_txt = CTkLabel(window, text=". . .", text_color=white, fg_color=lblue, bg_color=lblue, font=(boldfont, 20), width=156)
place_txt = CTkLabel(window, text=". . .", text_color=white, fg_color=lblue, bg_color=lblue, font=(boldfont, 20), wraplength=156, anchor='center', width=156, height=40)
date_txt = CTkLabel(window, text=". . .", text_color=white, fg_color=lblue, bg_color=lblue, font=(boldfont, 16), anchor='center',width=156, height=40)
time_txt = CTkLabel(window, text=". . .", text_color=white,fg_color=lblue, bg_color=lblue, font=(boldfont, 20), width=156)
currentmode_txt = CTkLabel(window, text=". . .", text_color=white, fg_color=lblue, bg_color=lblue, font=(boldfont, 20), width=156)

DESCRIPTION = CTkLabel(window, text="DESCRIPTION", text_color=lwhite, fg_color=lblue, bg_color=lblue, font=(boldfont, 20, 'bold'))
HUMIDITY = CTkLabel(window, text="HUMIDITY", text_color=lwhite, fg_color=lblue, bg_color=lblue, font=(boldfont, 20, 'bold'))
WIND = CTkLabel(window, text="WIND", text_color=lwhite, fg_color=lblue, bg_color=lblue, font=(boldfont, 20, 'bold'))
PRESSURE = CTkLabel(window, text="PRESSURE", text_color=lwhite, fg_color=lblue, bg_color=lblue, font=(boldfont, 20, 'bold'))

DESCRIPTIONInfo = CTkLabel(window, text="???", text_color="#353535", fg_color=lblue, bg_color=lblue, font=(boldfont, 20, 'bold'), width=180)
HUMIDITYInfo = CTkLabel(window, text="???", text_color="#353535", fg_color=lblue, bg_color=lblue, font=(boldfont, 20, 'bold'), width=100)
WINDInfo = CTkLabel(window, text="???", text_color="#353535", fg_color=lblue, bg_color=lblue, font=(boldfont, 20, 'bold'), width=100)
PRESSUREInfo = CTkLabel(window, text="???", text_color="#353535", fg_color=lblue, bg_color=lblue, font=(boldfont, 20, 'bold'), width=100)

#----ANIMATIONS-----
searchbtn.bind("<Enter>", lambda event: searchbtn.configure(image=Isearchbtn_hover))
searchbtn.bind("<Leave>", lambda event: searchbtn.configure(image=Isearch_btn))
refreshbtn.bind("<Enter>", lambda event: refreshbtn.configure(image=Irefreshbtn_hover))
refreshbtn.bind("<Leave>", lambda event: refreshbtn.configure(image=Irefresh_btn))

#----UTILITIES-----
location.bind('<Return>', handle_enter)

#----PLACEMENTS-----
navbar.place(x=0, y=0)
searchbar.place(x=0, y=0)
searchbtn.place(x=268, y=0)
refreshbtn.place(x=350,y=0)
location.place(x=5, y=0)
detailsbar.place(x=0, y=40)
detailsbar_txt.place(x=64,y=80)
weather_img.place(x=595, y=180)
bluebar.place(x=75, y=460)

country_txt.place(x=5, y=45)
place_txt.place(x=175, y=40)
date_txt.place(x=345,y=40)
time_txt.place(x=517,y=45)
currentmode_txt.place(x=688,y=45)

text1.place(x=550, y=115)
text2.place(x=585, y=310)
text3.place(x=40, y=160)
DESCRIPTION.place(x=115, y=470)
HUMIDITY.place(x=327, y=470)
WIND.place(x=500, y=470)
PRESSURE.place(x=628, y=470)

DESCRIPTIONInfo.place(x=85, y=500)
HUMIDITYInfo.place(x=322, y=500)
WINDInfo.place(x=475, y=500)
PRESSUREInfo.place(x=625, y=500)

window.mainloop()
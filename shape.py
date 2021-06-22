import requests
#import os
from datetime import datetime

api_key = 'bcc83896ae18be6f1a2f4d95e4de8105'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %m %Y | %H:%M:%S")

l = "Weather Stats for - {}  || {}".format(location.upper(), date_time)
m = "Current temperature is: {:.2f} deg C".format(temp_city)
n =  "Current weather desc  :", weather_desc
o = " Current Humidity      :", hmdt, '%'
p = "Current wind speed    :", wind_spd ,'kmph'

file_dis = input("enter file name to display the content ")
fd = open(file_dis,"x")
fd.write(str(l))
fd.write("\n")
fd.write(str(m))
fd.write("\n")
fd.write(str(n))
fd.write("\n")
fd.write(str(o))
fd.write("\n")
fd.write(str(p))
fd.close()
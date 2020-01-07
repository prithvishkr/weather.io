import pyowm
import requests
import json
#get the location of the user
send_url = "http://api.ipstack.com/check?access_key=93384f87cd862eb953d503f20d348b6b"
geo_req = requests.get(send_url)
geo_json = json.loads(geo_req.text)
#Place_ID1 = geo_json['zip']
#Place_ID = int(Place_ID1)
city = geo_json['city']
region = geo_json['region_name']
latitude = geo_json['latitude']
longitude = geo_json['longitude']
#we got the location
#get the weather
owm = pyowm.OWM('f883d296b615dc7e68ba90881eb138db')
P_weather = owm.weather_at_coords(latitude,longitude) #we store all the info in P_weather
time1 = P_weather.get_reception_time(timeformat='iso')
weather = P_weather.get_weather()
time = weather.get_reference_time(timeformat='iso')
temperature = weather.get_temperature(unit='celsius')
wind_speed = weather.get_wind()
sun_rise = weather.get_sunrise_time(timeformat='iso')
sun_set = weather.get_sunset_time(timeformat='iso')
print(city)
print(region)
print(time)
print(time1)
print(temperature)
print(wind_speed)
print(sun_rise)
print(sun_set)

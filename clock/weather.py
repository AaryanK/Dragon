import pyowm


def weather_info():
    owm=pyowm.OWM('b318d9f28024e9e56d74dd853a43de5b')
    location=owm.weather_at_place(f'Kathmandu')
    weather=location.get_weather()
    temp=weather.get_temperature('celsius')
    # humidity=weather.get_humidity()
    current_temp=temp['temp']
    return current_temp

def weather_at_place(city):
    owm=pyowm.OWM('b318d9f28024e9e56d74dd853a43de5b')
    location=owm.weather_at_place(f'{city}')
    weather=location.get_weather()
    temp=weather.get_temperature('celsius')
    # # humidity=weather.get_humidity()
    current_temp=temp['temp']
    return current_temp
    
    
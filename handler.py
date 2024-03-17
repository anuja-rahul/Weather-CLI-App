from python_datalogger import DataLogger
from dotenv import load_dotenv
import datetime as dt
import requests
import os


class WeatherAPIHandler:
    load_dotenv()
    __WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
    __CITY = os.getenv("CITY")
    __base_url = "http://api.openweathermap.org/data/2.5/weather?"

    def __init__(self):
        self.__logger = DataLogger("WeatherAPIHandler", False, "INFO")
        self.__url = self.__base_url + "appid=" + self.__WEATHER_API_KEY + "&q=" + self.__CITY
        self.__response = requests.get(self.__url).json()

        self.__simplify_response()

    def __get_temps(self):
        temp_kelvin = self.__response['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        temp_fahrenheit = temp_celsius * (9 / 5) + 32
        return [f"{temp_kelvin:.02f} K", f"{temp_celsius:.02f} °c", f"{temp_fahrenheit:.02f} °F"]

    def __get_humidity(self):
        return self.__response['main']['humidity']

    def __get_wind_speed(self):
        return self.__response['wind']['speed']

    def __get_description(self):
        return self.__response['weather'][0]['description']

    def __get_sunrise_sunset(self):
        sunrise = dt.datetime.fromtimestamp(self.__response['sys']['sunrise'] + self.__response['timezone'])
        sunset = dt.datetime.fromtimestamp(self.__response['sys']['sunset'] + self.__response['timezone'])
        return [sunrise, sunset]

    def __simplify_response(self):
        self.__logger.log_info(f"<-----------------------Start of the Report----------------------->\n")
        self.__logger.log_info(f"City:          {self.__CITY}")
        self.__logger.log_info(f"Temperature:   {self.__get_temps()}")
        self.__logger.log_info(f"Humidity:      {self.__get_humidity()} %")
        self.__logger.log_info(f"Wind Speed:    {self.__get_wind_speed()} m/s, "
                               f"{(self.__get_wind_speed() * (18/5)):.02f} km/h")
        self.__logger.log_info(f"Description:   {self.__get_description()}")
        self.__logger.log_info(f"Sunrise:       {self.__get_sunrise_sunset()[0]}")
        self.__logger.log_info(f"Sunset:        {self.__get_sunrise_sunset()[1]}\n")
        self.__logger.log_info(f"<------------------------End of the Report------------------------>\n\n\n")





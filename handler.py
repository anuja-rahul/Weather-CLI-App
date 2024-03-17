from python_datalogger import DataLogger
from dotenv import load_dotenv
import datetime as dt
import requests
import os


class WeatherAPIHandler:
    load_dotenv()
    __WEATHER_API_TOKEN = os.getenv("WEATHER_API_TOKEN")

    def __init__(self):
        self.__logger = DataLogger("WeatherAPIHandler", True, "INFO")




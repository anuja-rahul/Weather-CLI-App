from python_datalogger import DataLogger
from handler import WeatherAPIHandler
from nuke import NukeFiles

test = WeatherAPIHandler()
nuke_user = NukeFiles(7, "logs/")

from handler import WeatherAPIHandler
from nuke import NukeFiles

test = WeatherAPIHandler()
nuke_user = NukeFiles(7, "logs/")
nuke_user.nuke_files()

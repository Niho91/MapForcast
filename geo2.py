from datetime import datetime 
from timezonefinder import TimezoneFinder
from pytz import timezone 
from sunnyday import Weather 
from folium import Marker

class Geopoint(Marker):
    
    def __init__(self, latitude, longitude, popup = None):
        super().__init__(location = [latitude, longitude], popup = popup)
        self.latitude = latitude
        self.longitude = longitude
    
    def closest_parallel(self):
        return round(self.latitude)

    def get_time(self):
        timezonefinder = TimezoneFinder()
        print(TimezoneFinder)
        timezone_string = timezonefinder.timezone_at(lng = self.longitude, lat = latitude)
        if timezone_string is None:
            return None
        else:
            tzone = timezone(timezone_string)
            time_now = datetime.now(tzone)
            return time_now
    
    def get_weather(self):
        weather = Weather(apikey = "00faebc1c90c786c85d1741fda41415c", lat = self.latitude, lon = self.longitude)
        return weather.next_12h_simplified()
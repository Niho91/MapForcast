from folium import Map, Marker, Popup
from geo2 import Geopoint

#Get latitude and longitude values
location = [[41, -1], [40, 2], [39, 5], [42, 6]]

#folium Map instance
mymap = Map(location = [40, 2])

for loc in location:
    #Create a Geopoint instance
    geopoint = Geopoint(latitude = loc[0], longitude = loc[1])
    forecast = geopoint.get_weather()
    popup_content = f"""
    {forecast[0][0][-8: -6]}h: {round(forecast[0][1])}°F <img src="http://openweathermap.org/img/wn/{forecast[0][-1]}@2x.png" width=35>
    <hr style="margin:1px">
    {forecast[1][0][-8: -6]}h: {round(forecast[1][1])}°F <img src="http://openweathermap.org/img/wn/{forecast[1][-1]}@2x.png" width=35>
    <hr style="margin:1px">
    {forecast[2][0][-8: -6]}h: {round(forecast[2][1])}°F <img src="http://openweathermap.org/img/wn/{forecast[2][-1]}@2x.png" width=35>
    <hr style="margin:1px">
    {forecast[3][0][-8: -6]}h: {round(forecast[3][1])}°F <img src="http://openweathermap.org/img/wn/{forecast[3][-1]}@2x.png" width=35>
    """

    popup = Popup(popup_content, max_width=400)
    popup.add_to(geopoint)
    geopoint.add_to(mymap)

#Save the Map instance into a html file

mymap.save("map.html")
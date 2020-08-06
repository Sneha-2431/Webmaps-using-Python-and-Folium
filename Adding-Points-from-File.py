import folium 
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])         #converting the data from dataframe list to python list
lon = list(data["LON"])

map2 = folium.Map(location=[36.58, -99.09], zoom_start=6, tiles="Stamen Terrain")
fg=folium.FeatureGroup(name="My Map")

for lt, ln in zip(lat, lon):    #zip function is used when we iterate through two lists at a time
    fg.add_child(folium.Marker(location=[lt, ln], popup="Hi I am a Marker", icon=folium.Icon(color='green')))

map2.add_child(fg)

map2.save("Map2.html")

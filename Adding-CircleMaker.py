import folium 
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])         #converting the data from dataframe list to python list
lon = list(data["LON"])
elev = list(data["ELEV"])

map2 = folium.Map(location=[36.58, -99.09], zoom_start=6, tiles="Stamen Terrain")
fg=folium.FeatureGroup(name="My Map")

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000 :
        return 'orange'
    else:
        return 'red'        

for lt, ln, el in zip(lat, lon, elev):    #zip function is used when we iterate through two lists at a time
    fg.add_child(folium.CircleMarker(location=[lt, ln], popup=str(el)+ " m",
    fill_color=color_producer(el), color = 'grey', fill_opacity = 0.7)) #popup attribute takes a string input

map2.add_child(fg)

map2.save("Map2.html")

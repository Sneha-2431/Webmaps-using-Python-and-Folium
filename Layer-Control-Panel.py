import folium 
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])         #converting the data from dataframe list to python list
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000 :
        return 'orange'
    else:
        return 'red'    

map2 = folium.Map(location=[36.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")            

for lt, ln, el in zip(lat, lon, elev):  #zip function is used when we iterate through two lists at a time
    fgv.add_child(folium.CircleMarker(location=[lt, ln], popup=str(el)+ " m",
    fill_color=color_producer(el), color = 'grey',
     fill_opacity = 0.7)) #popup attribute takes a string input

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data = open("world.json", "r" , encoding = "utf-8-sig").read(),
style_function = lambda x: {'fillColor' : 'green' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000<= x['properties']['POP2005'] < 20000000 else 'red'}))

map2.add_child(fgv)
map2.add_child(fgp)
map2.add_child(folium.LayerControl())  #LayerControl class 

map2.save("Map2.html")

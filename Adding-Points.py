import folium 
map2 = folium.Map(location=[36.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

fg=folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[36.2, -99.1], popup="Hi I am a Marker", icon=folium.Icon(color='green')))

map2.add_child(fg)

map2.save("Map2.html")

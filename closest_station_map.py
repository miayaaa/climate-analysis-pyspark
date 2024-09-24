import folium
from geopy.distance import geodesic

# Coordinates for the stations
wellington_coords = (-41.3272, 174.8052)  # Wellington Aero AWS
paraparaumu_coords = (-40.9044, 174.9894)  # Paraparaumu AWS

# Create a folium map
m = folium.Map(location=[(wellington_coords[0] + paraparaumu_coords[0]) / 2,
                         (wellington_coords[1] + paraparaumu_coords[1]) / 2], zoom_start=10)

# Add markers
distance_km = geodesic(wellington_coords, paraparaumu_coords).kilometers
folium.Marker(wellington_coords,
              popup=f"Wellington Aero AWS (NZM00093439)<br>Distance: {distance_km:.2f} km").add_to(m)
folium.Marker(paraparaumu_coords,
              popup=f"Paraparaumu AWS (NZ000093417)<br>Distance: {distance_km:.2f} km").add_to(m)

# Add a line between the two stations
folium.PolyLine(locations=[wellington_coords,
                paraparaumu_coords], color="blue").add_to(m)

# Save the map
m.save('stations_distance.html')

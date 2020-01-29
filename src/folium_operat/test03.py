import folium

# 地图上悬浮显示经纬度
m = folium.Map(
    location=[36.68159, 117.103565],
    zoom_start=10
)
m.add_child(folium.LatLngPopup())

# 手动打点功能
m.add_child(
    folium.ClickForMarker(popup='Waypoint')
)
m.save('f2.html')

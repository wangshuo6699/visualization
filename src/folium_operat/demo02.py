import folium
import numpy as np
import pandas as pd
from folium import plugins

full = pd.read_excel('./dat/2015Cities-CHINA.xlsx')
full = full.dropna()

# 创建地图对象：
schools_map = folium.Map(
    location=[full['lat'].mean(), full['lon'].mean()], zoom_start=5)
marker_cluster = plugins.MarkerCluster().add_to(schools_map)

# 标注数据点：
for name, row in full.iterrows():
    folium.Marker([row["lat"], row["lon"]], popup="{0}:{1}".format(
        row["cities"], row["GDP"])).add_to(marker_cluster)
    # folium.RegularPolygonMarker([row["lat"], row["lon"]], popup="{0}:{1}".format(
    #     row["cities"], row["GDP"]), number_of_sides=10, radius=10).add_to(marker_cluster)

schools_map.save('./res/schools_map.html')  # 保存到本地

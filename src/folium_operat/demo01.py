import folium
import numpy as np
import pandas as pd
from folium.plugins import HeatMap

posi = pd.read_excel('./dat/2015Cities-CHINA.xlsx')
posi = posi.dropna()

lat = np.array(posi["lat"][0:len(posi)])
lon = np.array(posi["lon"][0:len(posi)])
pop = np.array(posi["pop"][0:len(posi)], dtype=float)
gdp = np.array(posi["GDP"][0:len(posi)], dtype=float)
gdp_ave = np.array(posi["GDP_Average"][0:len(posi)], dtype=float)
data1 = [[lat[i], lon[i], gdp_ave[i]] for i in range(len(posi))]

# 创建以高德地图为底图的密度图：
map_osm = folium.Map(
    location=[35, 110],
    zoom_start=5,
    tiles='http://webrd02.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=8&x={x}&y={y}&z={z}',
    attr="&copy; <a href='http://ditu.amap.com/'>高德地图</a>"
)

# 生成交互式地图：
HeatMap(data1).add_to(map_osm)
file_path = './res/gdp_ave.html'
map_osm.save(file_path)

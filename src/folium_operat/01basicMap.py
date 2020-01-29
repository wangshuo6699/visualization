import os
import folium

m = folium.Map(location=[31.5785354300, 117.2900390600], zoom_start=14)

# tiles is url Map
map_osm = folium.Map(
    location=[35, 110],
    zoom_start=4,
    tiles='http://webrd02.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=8&x={x}&y={y}&z={z}',
    # tiles='http://webst02.is.autonavi.com/appmaptile?style=8&x={x}&y={y}&z={z}',
    attr="&copy; <a href='http://ditu.amap.com/'>高德地图</a>"
)

m.save('./result/test01.html')
map_osm.save('./result/gaode.html')

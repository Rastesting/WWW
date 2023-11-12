import sqlite3
import folium
from folium import plugins
from django.core.exceptions import PermissionDenied
from django.shortcuts import render

def test(h):
    print(h)
def index(request):
    if request.user.is_authenticated:
        print("Загружается карта")
        m = folium.Map(location=(60.15, 30.2), zoom_start=10, zoom_control=False)

        folium.plugins.Fullscreen(
            position="topright",
            title="Expand me",
            title_cancel="Exit me",
            force_separate_button=True,
        ).add_to(m)

        spb = folium.map.FeatureGroup()
        con = sqlite3.connect("db.sqlite3")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Points ORDER BY Adress DESC")#🟥
        for p in cursor.fetchall():
            if p[6] == '🟨' or p[6] == '🟩':
                place = p[7], p[8]
                description = ', ' + p[1] + p[2]
                if p[2] == '🛠':
                    spb.add_child(
                        folium.features.CircleMarker(place, radius=10,
                            color='red', fill_color='Red', popup=f"<a href=\"{'http://192.168.31.65/main/tab/'}\">{p[0]}</a>" + description))
                    m.add_child(spb)
                elif p[2] == '💰':
                    spb.add_child(
                        folium.features.CircleMarker(place, radius=10,
                            color='Blue', fill_color='Blue', popup=f"<a href=\"{'http://192.168.31.65/main/tab/'}\">{p[0]}</a>" + description))
                    m.add_child(spb)
                elif p[2] == '📝':
                    spb.add_child(
                        folium.features.CircleMarker(place, radius=10,
                            color='#000000', fill_color='#000000', popup=f"<a href=\"{'http://192.168.31.65/main/tab/'}\">{p[0]}</a>" + description))
                    m.add_child(spb)
                elif p[2] == '🚚':
                    spb.add_child(
                        folium.features.CircleMarker(place, radius=10,
                            color='#03AC13', fill_color='#03AC13', popup=f"<a href=\"{'http://192.168.31.65/main/tab/'}\">{p[0]}</a>" + description))
                    m.add_child(spb)
                else:
                    spb.add_child(
                        folium.features.CircleMarker(place, radius=10,
                            color='#FFFFFF', fill_color='#FFFFFF', popup=f"<a href=\"{'http://192.168.31.65/main/tab/'}\">{p[0]}</a>" + description))
                    m.add_child(spb)

        m.save("main/templates/map/index.html")
        print("Загруженна карта")
        return render(request,'map/index.html',{})

    else:
        raise PermissionDenied

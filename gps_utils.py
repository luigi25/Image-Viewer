import folium
from PyQt5.QtWebEngineWidgets import QWebEngineView
import io


def convert_to_degrees(value):
    d = float(value[0])
    m = float(value[1]) / 60.0
    s = float(value[2]) / 3600.0
    return d + m + s


def gps_view(gps_exif):
    latitude, longitude = None, None

    gps_latitude = gps_exif['GPSLatitude']
    gps_latitude_ref = gps_exif['GPSLatitudeRef']
    gps_longitude = gps_exif['GPSLongitude']
    gps_longitude_ref = gps_exif['GPSLongitudeRef']

    if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
        latitude = convert_to_degrees(gps_latitude)
        if gps_latitude_ref != 'N':
            latitude = 0 - latitude

        longitude = convert_to_degrees(gps_longitude)
        if gps_longitude_ref != 'E':
            longitude = 0 - longitude

    url = '<a href="https://www.google.com/maps/search/?api=1&query={0},{1}"> Google Maps </a>'.format(
        latitude, longitude)
    #print('url: {}'.format(url))

    coordinate = (latitude, longitude)
    m = folium.Map(title='GPS Location', zoom_start=18, location=coordinate)
    popup = folium.Popup(f'<h4>For more information go to {url}</h4>', max_width=len('For more information') * 9)
    folium.Marker(coordinate, popup=popup).add_to(m)
    # save map data to data object
    data = io.BytesIO()
    m.save(data, close_file=False)
    web_view = QWebEngineView()
    web_view.setHtml(data.getvalue().decode())
    return web_view

from PyQt5.QtWidgets import QFileDialog, QMainWindow, QTableWidgetItem, QDialog
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from Model import Model
from MainWindow import Ui_MainWindow
from ExifWindow import Ui_Dialog
import io
import folium
from PyQt5.QtWebEngineWidgets import QWebEngineView


class ExifViewer(QDialog):
    def __init__(self, exif, parent=None):
        super(ExifViewer, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.exif = exif
        self.populate_table()
        self.file_name = None
        self.gps = None

    def populate_table(self):
        self.gps = self.exif.pop('GPSInfo') if ('GPSInfo' in self.exif) else None
        if self.gps:
            self.ui.tableWidget.setRowCount(len(self.exif) + len(self.gps))
            for r, tag in enumerate(self.exif):
                self.ui.tableWidget.setItem(r, 0, QTableWidgetItem(tag))
                self.ui.tableWidget.setItem(r, 1, QTableWidgetItem(str(self.exif[tag])))

            for r, tag in enumerate(self.gps):
                self.ui.tableWidget.setItem(len(self.exif) + r, 0, QTableWidgetItem(tag))
                self.ui.tableWidget.setItem(len(self.exif) + r, 1, QTableWidgetItem(str(self.gps[tag])))

            lat, lon = self.get_exif_location(self.gps)
            url = '<a href="https://www.google.com/maps/search/?api=1&query={0},{1}"> Link to Google Maps </a>'.format(
                lat, lon)
            print('url: {}'.format(url))
            self.ui.link_maps.setText(url)

            coordinate = (lat, lon)
            m = folium.Map(title='GPS Location', zoom_start=15, location=coordinate)
            popup = folium.Popup(f'<h4>For more info click here: {url}</h4>', max_width=len('For more info click here:')* 8)
            folium.Marker(coordinate, popup=popup).add_to(m)
            # save map data to data object
            data = io.BytesIO()
            m.save(data, close_file=False)
            web_view = QWebEngineView()
            web_view.setHtml(data.getvalue().decode())
            self.ui.gridLayout_2.addWidget(web_view, 0, 0, 1, 1)

        else:
            self.ui.tableWidget.setRowCount(len(self.exif))
            for r, tag in enumerate(self.exif):
                self.ui.tableWidget.setItem(r, 0, QTableWidgetItem(tag))
                self.ui.tableWidget.setItem(r, 1, QTableWidgetItem(str(self.exif[tag])))

    def convert_to_degress(self, value):
        d = float(value[0])
        m = float(value[1])
        s = float(value[2])
        return d + (m / 60.0) + (s / 3600.0)

    def get_exif_location(self, gpsexif):
        lat = None
        lon = None

        gps_latitude = gpsexif['GPSLatitude']
        gps_latitude_ref = gpsexif['GPSLatitudeRef']
        gps_longitude = gpsexif['GPSLongitude']
        gps_longitude_ref = gpsexif['GPSLongitudeRef']

        if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
            lat = self.convert_to_degress(gps_latitude)
            if gps_latitude_ref != 'N':
                lat = 0 - lat

            lon = self.convert_to_degress(gps_longitude)
            if gps_longitude_ref != 'E':
                lon = 0 - lon

        return lat, lon


class ImgViewer(QMainWindow):
    def __init__(self, model: Model):
        super(ImgViewer, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.model = model

        self.width = None
        self.height = None
        self.ratio = None

        self.show()

        self.interaction()

    def interaction(self):
        self.ui.action_open.triggered.connect(self.clicked_open)
        self.ui.ccw_rotate.triggered.connect(self.left_rotate)
        self.ui.cw_rotate.triggered.connect(self.right_rotate)
        self.ui.current_img.triggered.connect(self.close_img)
        self.ui.action_exif.triggered.connect(lambda: self.get_exif_info())

    def clicked_open(self):
        self.file_name = QFileDialog.getOpenFileName(None, "Open File", '/home',
                                                     "jpeg images (*.jpg *.jpeg *.JPG)")
        min_size = 512
        if self.file_name[0]:
            # open the image
            self.pixmap = QPixmap(self.file_name[0])
            self.width = self.pixmap.width()
            self.height = self.pixmap.height()
            ratio = self.width / self.height
            self.width, self.height = (min_size, int(min_size / ratio)) if (self.width > self.height) else (int(ratio * min_size), min_size)
            # add pic to label
            self.ui.image_label.setPixmap(self.pixmap.scaled(self.width, self.height, Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def left_rotate(self):
        if self.ui.image_label.pixmap():
            self.rotate = True
            self.rotation = QTransform().rotate(-90.0)

            self.pixmap = self.pixmap.transformed(self.rotation, Qt.SmoothTransformation)


            # add pic to label
            self.ui.image_label.setPixmap(self.pixmap.scaled(self.width, self.height, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.rotation = 0

    def right_rotate(self):
        if self.ui.image_label.pixmap():
            self.rotate = True
            self.rotation = QTransform().rotate(90.0)

            self.pixmap = self.pixmap.transformed(self.rotation, Qt.SmoothTransformation)

            # add pic to label
            self.ui.image_label.setPixmap(self.pixmap.scaled(self.width, self.height, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.rotation = 0

    def close_img(self):
        # close image
        self.ui.image_label.setPixmap(QPixmap())

    def get_exif_info(self):
        if self.ui.image_label.pixmap():
            exif = self.model.get_exif(self.file_name[0])
            if exif:
                exif_viewer = ExifViewer(exif, self)
                exif_viewer.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    im_viewer = ImgViewer(Model())
    im_viewer.show()
    sys.exit(app.exec_())

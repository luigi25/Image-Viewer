from PyQt5.QtWidgets import QFileDialog, QMainWindow, QTableWidgetItem, QDialog, QMessageBox
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets, QtCore, QtGui
from Model import Model
from MainWindow import Ui_MainWindow
from ExifWindow import Ui_Dialog
import io
import folium
from PyQt5.QtWebEngineWidgets import QWebEngineView
import qdarkstyle


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

            latitude, longitude = self.get_exif_location(self.gps)
            url = '<a href="https://www.google.com/maps/search/?api=1&query={0},{1}"> Google Maps </a>'.format(
                latitude, longitude)
            print('url: {}'.format(url))
            self.ui.link_maps.setText(url)

            coordinate = (latitude, longitude)
            m = folium.Map(title='GPS Location', zoom_start=18, location=coordinate)
            popup = folium.Popup(f'<h4>For more info go to {url}</h4>', max_width=len('For more info go to') * 8)
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
        m = float(value[1]) / 60.0
        s = float(value[2]) / 3600.0
        return d + m + s

    def get_exif_location(self, gpsexif):
        latitude, longitude = None, None

        gps_latitude = gpsexif['GPSLatitude']
        gps_latitude_ref = gpsexif['GPSLatitudeRef']
        gps_longitude = gpsexif['GPSLongitude']
        gps_longitude_ref = gpsexif['GPSLongitudeRef']

        if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
            latitude = self.convert_to_degress(gps_latitude)
            if gps_latitude_ref != 'N':
                latitude = 0 - latitude

            longitude = self.convert_to_degress(gps_longitude)
            if gps_longitude_ref != 'E':
                longitude = 0 - longitude

        return latitude, longitude


class ImgViewer(QMainWindow):
    def __init__(self, model: Model):
        super(ImgViewer, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.model = model

        # self.width = None
        # self.height = None
        self.ratio = None
        self.file_name = None
        self.pixmap = None

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
        if self.file_name[0]:
            # open the image
            self.pixmap = QPixmap(self.file_name[0])

            self.size_img(self.pixmap.width(), self.pixmap.height())

            self.ui.ccw_rotate.setEnabled(True)
            self.ui.cw_rotate.setEnabled(True)
            self.ui.close_images.setEnabled(True)
            self.ui.action_exif.setEnabled(True)

        else:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle('Selection Error')
            msg_box.setWindowIcon(QtGui.QIcon('icons/exclamation.png'))
            msg_box.setText("No images have been selected")
            msg_box.exec_()


    def size_img(self, width, height):
        min_size = 512
        if width > height:
            self.ui.image_label.setPixmap(
                self.pixmap.scaled(QSize(self.ui.image_label.width(), min(self.ui.image_label.height(), min_size)),
                                   Qt.KeepAspectRatio, Qt.SmoothTransformation))
        else:
            self.ui.image_label.setPixmap(
                self.pixmap.scaled(QSize(min(self.ui.image_label.width(), min_size), self.ui.image_label.height()),
                                   Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def resizeEvent(self, ev):
        if self.file_name and self.pixmap:
            self.size_img(self.pixmap.width(), self.pixmap.height())
        super().resizeEvent(ev)

    def left_rotate(self):
        if self.file_name:
            self.rotate = True
            self.rotation = QTransform().rotate(-90.0)

            self.pixmap = self.pixmap.transformed(self.rotation, Qt.SmoothTransformation)
            self.size_img(self.pixmap.width(), self.pixmap.height())

            self.rotation = 0

    def right_rotate(self):
        if self.file_name:
            self.rotate = True
            self.rotation = QTransform().rotate(90.0)

            self.pixmap = self.pixmap.transformed(self.rotation, Qt.SmoothTransformation)
            self.size_img(self.pixmap.width(), self.pixmap.height())

            self.rotation = 0

    def close_img(self):
        # close image
        if self.file_name:
            self.file_name = None
            self.ui.image_label.setPixmap(QtGui.QPixmap("icons/add_img.PNG"))
            self.ui.ccw_rotate.setDisabled(True)
            self.ui.cw_rotate.setDisabled(True)
            self.ui.close_images.setDisabled(True)
            self.ui.action_exif.setDisabled(True)

    def get_exif_info(self):
        if self.file_name:
            exif = self.model.get_exif(self.file_name[0])
            exif_viewer = ExifViewer(exif, self)
            exif_viewer.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    im_viewer = ImgViewer(Model())
    im_viewer.show()
    sys.exit(app.exec_())

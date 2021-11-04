from PyQt5.QtWidgets import QFileDialog, QMainWindow, QTableWidgetItem, QDialog
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from Model import Model
from MainWindow import Ui_MainWindow
from ExifWindow import Ui_Dialog


class ExifViewer(QDialog):
    def __init__(self, exif, parent=None):
        super(ExifViewer, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.exif = exif
        self.populate_table()
        self.file_name = None

    def populate_table(self):
        # gps = self.exif.pop('GPSInfo') if ('GPSInfo' in self.exif) else None
        self.ui.tableWidget.setRowCount(len(self.exif))
        for r, tag in enumerate(self.exif):
            self.ui.tableWidget.setItem(r, 0, QTableWidgetItem(tag))
            self.ui.tableWidget.setItem(r, 1, QTableWidgetItem(str(self.exif[tag])))
        # if gps is not None:
        #     lat, lon = get_exif_location(gps)
        #     url = '<a href="https://www.google.com/maps/search/?api=1&query={0},{1}"> Link to Google Maps </a>'.format(
        #         lat, lon)
        #     print('url: {}'.format(url))
        #     self.ui.webLabel.setText(url)


class ImgViewer(QMainWindow):
    def __init__(self, model: Model):
        super(ImgViewer, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.model = model
        self.show()

        self.build_behavior()

    def build_behavior(self):
        self.ui.action_open.triggered.connect(self.clicked_open)
        self.ui.ccw_rotate.triggered.connect(self.left_rotate)
        self.ui.cw_rotate.triggered.connect(self.right_rotate)
        self.ui.current_img.triggered.connect(self.close_img)
        self.ui.action_exif.triggered.connect(lambda: self.get_exif_info())

    def clicked_open(self):
        self.file_name = QFileDialog.getOpenFileName(None, "Open File", '/home',
                                            "jpeg images (*.jpg *.jpeg *.JPG)")

        # open the image
        self.pixmap = QPixmap(self.file_name[0])
        w = self.pixmap.width()
        h = self.pixmap.height()
        # add pic to label
        self.ui.image_label.setPixmap(self.pixmap.scaled(w, h, Qt.KeepAspectRatioByExpanding))

    def left_rotate(self):
        if self.ui.image_label.pixmap():
            self.rotate = True
            self.rotation = QTransform().rotate(-90.0)

            # transform = QTransform().rotate(self.rotation)
            self.pixmap = self.pixmap.transformed(self.rotation, Qt.SmoothTransformation)

            # add pic to label
            self.ui.image_label.setPixmap(self.pixmap)
            self.rotation = 0

    def right_rotate(self):
        if self.ui.image_label.pixmap():
            self.rotate = True
            self.rotation = QTransform().rotate(90.0)

            # transform = QTransform().rotate(self.rotation)
            self.pixmap = self.pixmap.transformed(self.rotation, Qt.SmoothTransformation)

            # add pic to label
            self.ui.image_label.setPixmap(self.pixmap)
            self.rotation = 0

    def close_img(self):
        # close image
        self.ui.image_label.setPixmap(QPixmap())

    def get_exif_info(self):
        if self.ui.image_label.pixmap():
            exif = self.model.get_exif(self.file_name[0])
            exif_viewer = ExifViewer(exif, self)
            exif_viewer.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    im_viewer = ImgViewer(Model())
    im_viewer.show()
    sys.exit(app.exec_())

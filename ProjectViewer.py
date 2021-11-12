from PyQt5.QtWidgets import QFileDialog, QMainWindow, QTableWidgetItem, QDialog, QMessageBox
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets, QtGui, QtCore
from Model import Model
from ImageWindowUI import Ui_MainWindow
from ExifWindowUI import Ui_Dialog
import io
import folium
from PyQt5.QtWebEngineWidgets import QWebEngineView
import qdarkstyle
from gps_utils import gps_view


class ExifViewer(QDialog):
    def __init__(self, exif, parent=None):
        super(ExifViewer, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.exif = exif
        self.fill_table()

    def fill_table(self):
        gps = self.exif.pop('GPSInfo') if ('GPSInfo' in self.exif) else None
        if gps:
            self.ui.tableWidget.setRowCount(len(self.exif) + len(gps))
            for r, tag in enumerate(self.exif):
                self.ui.tableWidget.setItem(r, 0, QTableWidgetItem(tag))
                self.ui.tableWidget.setItem(r, 1, QTableWidgetItem(str(self.exif[tag])))

            for r, tag in enumerate(gps):
                self.ui.tableWidget.setItem(len(self.exif) + r, 0, QTableWidgetItem(tag))
                self.ui.tableWidget.setItem(len(self.exif) + r, 1, QTableWidgetItem(str(gps[tag])))

            gps_location = gps_view(gps)
            # visualize the map of gps info in exif data
            self.ui.gridLayout_2.addWidget(gps_location, 0, 0, 1, 1)

        else:
            self.ui.tableWidget.setRowCount(len(self.exif))
            for r, tag in enumerate(self.exif):
                self.ui.tableWidget.setItem(r, 0, QTableWidgetItem(tag))
                self.ui.tableWidget.setItem(r, 1, QTableWidgetItem(str(self.exif[tag])))


class ImgViewer(QMainWindow):
    def __init__(self, model: Model):
        super(ImgViewer, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.model = model

        self.show()
        self.interaction()

    def resizeEvent(self, ev):
        if self.model.file_name and self.model.pixmap:
            self.set_aspect_ratio(self.model.pixmap.width(), self.model.pixmap.height())
        super().resizeEvent(ev)

    def interaction(self):
        self.ui.action_open.triggered.connect(self.open_img)
        self.ui.ccw_rotate.triggered.connect(self.left_rotate)
        self.ui.cw_rotate.triggered.connect(self.right_rotate)
        self.ui.current_img.triggered.connect(self.close_img)
        self.ui.action_exif.triggered.connect(self.show_exif)

    def open_img(self):
        file_dialog = QFileDialog()
        options = file_dialog.Options()
        options |= file_dialog.DontUseNativeDialog
        file_dialog.setGeometry(560, 290, 800, 480)
        file_dialog.setWindowIcon(QtGui.QIcon("icons/application-dialog.png"))
        self.model.file_name = file_dialog.getOpenFileName(file_dialog, "Open File", '/home',
                                                           "jpeg images (*.jpg *.jpeg *.JPG)", options=options)
        if self.model.file_name[0]:
            # open the image
            self.model.pixmap = QPixmap(self.model.file_name[0])
            self.set_aspect_ratio(self.model.pixmap.width(), self.model.pixmap.height())
            self.set_tools_enabled()

        else:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle('Selection Error')
            msg_box.setWindowIcon(QtGui.QIcon('icons/exclamation.png'))
            msg_box.setText("No images have been selected")
            msg_box.exec_()

    def set_aspect_ratio(self, width, height):
        max_size = 512
        if width > height:
            self.ui.image_label.setPixmap(
                self.model.pixmap.scaled(
                    QSize(self.ui.image_label.width(), min(self.ui.image_label.height(), max_size)),
                    Qt.KeepAspectRatio, Qt.SmoothTransformation))
        else:
            self.ui.image_label.setPixmap(
                self.model.pixmap.scaled(
                    QSize(min(self.ui.image_label.width(), max_size), self.ui.image_label.height()),
                    Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def left_rotate(self):
        if self.model.file_name:
            rotation = QTransform().rotate(-90.0)
            self.model.pixmap = self.model.pixmap.transformed(rotation, Qt.SmoothTransformation)
            self.set_aspect_ratio(self.model.pixmap.width(), self.model.pixmap.height())

    def right_rotate(self):
        if self.model.file_name:
            rotation = QTransform().rotate(90.0)

            self.model.pixmap = self.model.pixmap.transformed(rotation, Qt.SmoothTransformation)
            self.set_aspect_ratio(self.model.pixmap.width(), self.model.pixmap.height())

    def close_img(self):
        # close image
        if self.model.file_name:
            self.model.file_name = None
            self.ui.image_label.setPixmap(QtGui.QPixmap("icons/add_img.PNG"))
            self.set_tools_disabled()

    def show_exif(self):
        if self.model.file_name:
            exif = self.model.get_exif(self.model.file_name[0])
            exif_viewer = ExifViewer(exif, self)
            exif_viewer.show()

    def set_tools_enabled(self):
        self.ui.ccw_rotate.setEnabled(True)
        self.ui.cw_rotate.setEnabled(True)
        self.ui.close_images.setEnabled(True)
        self.ui.action_exif.setEnabled(True)

    def set_tools_disabled(self):
        self.ui.ccw_rotate.setDisabled(True)
        self.ui.cw_rotate.setDisabled(True)
        self.ui.close_images.setDisabled(True)
        self.ui.action_exif.setDisabled(True)


# if __name__ == "__main__":
#     import sys
#
#     app = QtWidgets.QApplication(sys.argv)
#     app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
#
#     im_viewer = ImgViewer(Model())
#     im_viewer.show()
#     sys.exit(app.exec_())

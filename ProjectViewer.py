from PyQt5.QtWidgets import QFileDialog, QMainWindow, QTableWidgetItem, QDialog, QMessageBox
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets, QtGui, QtCore
from Model import Model
from ImageWindowUI import Ui_MainWindow
from ExifWindowUI import Ui_Dialog
from gps_utils import gps_map


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

            gps_location = gps_map(gps)
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
        self.file_names = list()
        self.items = list()
        self.current_item = -1
        self.ui.list_widget.hide()

        self.show()
        self.interaction()

    def resizeEvent(self, ev):
        if self.model.images and self.ui.close_option.isEnabled():
            self.set_aspect_ratio()
        super().resizeEvent(ev)

    def keyPressEvent(self, qKeyEvent):
        if qKeyEvent.key() == QtCore.Qt.Key_Return:
            self.update_img()
        else:
            super().keyPressEvent(qKeyEvent)

    def interaction(self):
        self.ui.action_open.triggered.connect(self.open_img)
        self.ui.ccw_rotate.triggered.connect(self.left_rotate)
        self.ui.cw_rotate.triggered.connect(self.right_rotate)
        self.ui.close_img.triggered.connect(self.close_img)
        self.ui.close_all_img.triggered.connect(self.close_all_images)
        self.ui.action_exif.triggered.connect(self.show_exif)
        self.ui.side_list.triggered.connect(self.toggle_img_list)
        self.ui.list_widget.itemDoubleClicked.connect(self.update_img)

    def open_img(self):
        file_dialog = QFileDialog()
        options = file_dialog.Options()
        options |= file_dialog.DontUseNativeDialog
        file_dialog.setGeometry(560, 290, 800, 480)
        file_dialog.setWindowIcon(QtGui.QIcon("icons/application-dialog.png"))
        f_name = file_dialog.getOpenFileName(file_dialog, "Open File", '/home',
                                             "jpeg images (*.jpg *.jpeg *.JPG)", options=options)
        if f_name[0]:
            # open the image
            self.model.pixmap = QPixmap(f_name[0])
            item = QtWidgets.QListWidgetItem(f_name[0].split('/')[-1])
            icon = QtGui.QIcon()
            icon.addPixmap(self.model.pixmap, QtGui.QIcon.Normal)
            item.setIcon(icon)
            if item.text() not in self.items:
                self.items.append(item.text())
                self.file_names.append(f_name[0])
                self.model.images.append(self.model.pixmap)
                self.ui.list_widget.addItem(item)
                self.ui.list_widget.setCurrentRow(len(self.ui.list_widget) - 1)
                self.update_img()
                self.ui.side_list.setChecked(True)
                self.toggle_img_list()
        else:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle('Selection Error')
            msg_box.setWindowIcon(QtGui.QIcon('icons/exclamation.png'))
            msg_box.setText("No images have been selected")
            msg_box.exec_()

    def update_img(self):
        self.current_item = self.ui.list_widget.currentRow()
        self.model.get_current_img(self.current_item)  # Get image from model
        self.model.pixmap = self.model.current_image
        self.set_aspect_ratio()
        self.set_tools_enabled()

    def set_aspect_ratio(self):
        max_size = 512
        self.ui.image_label.setPixmap(
            self.model.pixmap.scaled(
                QSize(min(self.ui.image_label.width(), max_size), min(self.ui.image_label.height(), max_size)),
                Qt.KeepAspectRatio, Qt.FastTransformation))

    def left_rotate(self):
        if self.model.pixmap:
            rotation = QTransform().rotate(-90.0)
            self.model.pixmap = self.model.pixmap.transformed(rotation, Qt.FastTransformation)
            self.set_aspect_ratio()

    def right_rotate(self):
        if self.model.pixmap:
            rotation = QTransform().rotate(90.0)
            self.model.pixmap = self.model.pixmap.transformed(rotation, Qt.FastTransformation)
            self.set_aspect_ratio()

    def close_img(self):
        # close image
        if len(self.ui.list_widget.selectedItems()) != 0:
            self.current_item = self.ui.list_widget.currentRow()
            self.model.delete_current_img(self.current_item)
            self.ui.list_widget.takeItem(self.current_item)
            self.items.pop(self.current_item)
            self.file_names.pop(self.current_item)
            self.ui.image_label.setPixmap(QtGui.QPixmap("icons/add_img.PNG"))
            self.set_tools_disabled()
            if not self.model.images:
                self.ui.side_list.setChecked(False)
                self.ui.list_widget.hide()

    def close_all_images(self):
        if len(self.ui.list_widget.selectedItems()) != 0:
            self.model.empty_list()
            del self.items[:]
            del self.file_names[:]
            self.ui.list_widget.clear()
            self.ui.image_label.setPixmap(QtGui.QPixmap("icons/add_img.PNG"))
            self.set_tools_disabled()
            self.ui.side_list.setChecked(False)
            self.ui.list_widget.hide()

    def show_exif(self):
        if self.model.pixmap:
            self.current_item = self.ui.list_widget.currentRow()
            exif = self.model.get_exif(self.file_names[self.current_item])
            exif_viewer = ExifViewer(exif, self)
            exif_viewer.show()

    def toggle_img_list(self):
        # show/hide side list
        if self.ui.side_list.isChecked() is False:
            self.ui.list_widget.hide()
        else:
            self.ui.list_widget.show()

    def set_tools_enabled(self):
        self.ui.ccw_rotate.setEnabled(True)
        self.ui.cw_rotate.setEnabled(True)
        self.ui.close_option.setEnabled(True)
        self.ui.action_exif.setEnabled(True)

    def set_tools_disabled(self):
        self.ui.ccw_rotate.setDisabled(True)
        self.ui.cw_rotate.setDisabled(True)
        self.ui.close_option.setDisabled(True)
        self.ui.action_exif.setDisabled(True)
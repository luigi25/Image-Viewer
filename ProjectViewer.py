from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt, QSize, QFileInfo
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QTableWidgetItem, QDialog, QMessageBox
from Model import Model
from ExifWindowUI import Ui_Dialog
from ImageWindowUI import Ui_MainWindow
from gps_utils import gps_map
from itertools import cycle


class ExifViewer(QDialog):
    def __init__(self, info, exif, parent=None):
        super(ExifViewer, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.info = info
        self.exif = exif
        self.fill_table()

    def fill_table(self):
        gps = self.exif.pop('GPSInfo') if ('GPSInfo' in self.exif) else None
        if self.info:
            self.ui.tableWidget.setRowCount(len(self.info))
            for r, tag in enumerate(self.info):
                self.ui.tableWidget.setItem(r, 0, QTableWidgetItem(tag))
                self.ui.tableWidget.setItem(r, 1, QTableWidgetItem(str(self.info[tag])))

        if gps:
            self.ui.tableWidget1.setRowCount(len(self.exif) + len(gps))
            for r, tag in enumerate(self.exif):
                self.ui.tableWidget1.setItem(r, 0, QTableWidgetItem(tag))
                self.ui.tableWidget1.setItem(r, 1, QTableWidgetItem(str(self.exif[tag])))

            for r, tag in enumerate(gps):
                self.ui.tableWidget1.setItem(len(self.exif) + r, 0, QTableWidgetItem(tag))
                self.ui.tableWidget1.setItem(len(self.exif) + r, 1, QTableWidgetItem(str(gps[tag])))

            gps_location = gps_map(gps)
            # visualize the map of gps info in exif data
            self.ui.gridLayout_2.addWidget(gps_location, 0, 0, 1, 1)

        else:
            self.ui.tableWidget1.setRowCount(len(self.exif))
            for r, tag in enumerate(self.exif):
                self.ui.tableWidget1.setItem(r, 0, QTableWidgetItem(tag))
                self.ui.tableWidget1.setItem(r, 1, QTableWidgetItem(str(self.exif[tag])))


class ImgViewer(QMainWindow):
    def __init__(self, model: Model):
        super(ImgViewer, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.model = model
        self.file_names = list()
        self.current_item = -1
        self.ui.list_widget.hide()

        self.show()
        self.interaction()

    def resizeEvent(self, ev):
        if self.model.images and self.ui.close_option.isEnabled():
            self.set_aspect_ratio()
        super().resizeEvent(ev)

    def keyPressEvent(self, key_event):
        if key_event.key() == Qt.Key_Return:
            self.update_img()
        else:
            super().keyPressEvent(key_event)

    def dragEnterEvent(self, e):
        if len(e.mimeData().urls()) > 0 and e.mimeData().urls()[0].isLocalFile():
            qi = QFileInfo(e.mimeData().urls()[0].toLocalFile())
            ext = qi.suffix()
            if ext == 'jpg' or ext == 'jpeg' or ext == 'png' or ext == 'JPG' or ext == 'PNG':
                e.accept()
            else:
                e.ignore()
        else:
            e.ignore()

    def dropEvent(self, e):
        if e.mimeData().hasUrls:
            e.setDropAction(Qt.CopyAction)
            e.accept()
            for url in e.mimeData().urls():
                f_name = str(url.toLocalFile())
                self.open_img(f_name)
        else:
            e.ignore()

    def contextMenuEvent(self, event):
        action = self.ui.context_menu.exec_(self.mapToGlobal(event.pos()))
        if action == self.ui.open_context:
            self.open_img()
        elif action == self.ui.close_context:
            self.close_img()
        elif action == self.ui.close_all_context:
            self.close_all_images()
        elif action == self.ui.cw_rotate_context:
            self.right_rotate()
        elif action == self.ui.ccw_rotate_context:
            self.left_rotate()
        elif action == self.ui.info_context:
            self.show_img_info()
        elif action == self.ui.list_context:
            self.toggle_img_list()

    def interaction(self):
        self.ui.action_open.triggered.connect(self.open_img)
        self.ui.ccw_rotate.triggered.connect(self.left_rotate)
        self.ui.cw_rotate.triggered.connect(self.right_rotate)
        self.ui.close_img.triggered.connect(self.close_img)
        self.ui.close_all_img.triggered.connect(self.close_all_images)
        self.ui.get_info.triggered.connect(self.show_img_info)
        self.ui.side_list.triggered.connect(self.toggle_img_list)
        self.ui.list_widget.itemDoubleClicked.connect(self.update_img)

    def open_img(self, f_name=None):
        # choose f_name from file_dialog if is None
        if not f_name:
            file_dialog = QFileDialog()
            options = file_dialog.Options()
            options |= file_dialog.DontUseNativeDialog
            file_dialog.setGeometry(560, 290, 800, 480)
            file_dialog.setWindowIcon(QtGui.QIcon("icons/application-dialog.png"))
            f_name, _ = file_dialog.getOpenFileName(file_dialog, "Open File", '/home',
                                                    "Images (*.jpg *.jpeg *.png *.JPG *.PNG)", options=options)

        # check if f_name is selected, else a warning message is shown
        if f_name:
            if f_name not in self.file_names:
                self.file_names.append(f_name)
                self.model.images.append(QtGui.QPixmap(f_name))
                item = QtWidgets.QListWidgetItem(f_name.split('/')[-1])
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(f_name), QtGui.QIcon.Normal)
                item.setIcon(icon)
                self.ui.list_widget.addItem(item)
                self.ui.list_widget.setCurrentRow(len(self.ui.list_widget) - 1)
                self.update_img()
                if len(self.ui.list_widget) >= 1:
                    self.ui.list_widget.show()
                    self.ui.list_widget.setSelectionMode(True)
        else:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle('Warning')
            msg_box.setWindowIcon(QtGui.QIcon('icons/exclamation.png'))
            msg_box.setText("No image selected")
            msg_box.exec_()

    def update_img(self):
        self.current_item = self.ui.list_widget.currentRow()
        self.model.set_current_img(self.current_item)  # Get image from model
        self.set_aspect_ratio()
        self.set_tools_enabled()

    def set_aspect_ratio(self):
        max_size = 512
        self.ui.image_label.setPixmap(
            self.model.current_image.scaled(
                QSize(min(self.ui.image_label.width(), max_size), min(self.ui.image_label.height(), max_size)),
                Qt.KeepAspectRatio, Qt.FastTransformation))

    def left_rotate(self):
        if self.model.current_image:
            rotation = QtGui.QTransform().rotate(-90.0)
            self.model.current_image = self.model.current_image.transformed(rotation, Qt.FastTransformation)
            self.set_aspect_ratio()

    def right_rotate(self):
        if self.model.current_image:
            rotation = QtGui.QTransform().rotate(90.0)
            self.model.current_image = self.model.current_image.transformed(rotation, Qt.FastTransformation)
            self.set_aspect_ratio()

    def close_img(self):
        # close image
        if len(self.ui.list_widget.selectedItems()) != 0:
            self.current_item = self.ui.list_widget.currentRow()
            self.model.delete_current_img(self.current_item)
            self.ui.list_widget.takeItem(self.current_item)
            self.file_names.pop(self.current_item)
            self.ui.image_label.setPixmap(QtGui.QPixmap("icons/add_img.PNG"))
            self.set_tools_disabled()
            if not self.model.images:
                self.ui.list_widget.hide()

    def close_all_images(self):
        if len(self.ui.list_widget.selectedItems()) != 0:
            self.model.empty_list()
            del self.file_names[:]
            self.ui.list_widget.clear()
            self.ui.image_label.setPixmap(QtGui.QPixmap("icons/add_img.PNG"))
            self.set_tools_disabled()
            self.ui.list_widget.hide()

    def show_img_info(self):
        if self.model.current_image:
            self.current_item = self.ui.list_widget.currentRow()
            info = self.model.extract_general_info(self.file_names[self.current_item])
            exif = self.model.extract_exif(self.file_names[self.current_item])
            exif_viewer = ExifViewer(info, exif, self)
            exif_viewer.show()

    def toggle_img_list(self):
        # show/hide side list
        if self.ui.list_widget.isHidden():
            self.ui.list_widget.show()
        else:
            self.ui.list_widget.hide()

    def set_tools_enabled(self):
        self.ui.ccw_rotate.setEnabled(True)
        self.ui.cw_rotate.setEnabled(True)
        self.ui.close_option.setEnabled(True)
        self.ui.get_info.setEnabled(True)
        self.ui.ccw_rotate_context.setEnabled(True)
        self.ui.cw_rotate_context.setEnabled(True)
        self.ui.close_context.setEnabled(True)
        self.ui.close_all_context.setEnabled(True)
        self.ui.info_context.setEnabled(True)

    def set_tools_disabled(self):
        self.ui.ccw_rotate.setDisabled(True)
        self.ui.cw_rotate.setDisabled(True)
        self.ui.close_option.setDisabled(True)
        self.ui.get_info.setDisabled(True)
        self.ui.ccw_rotate_context.setDisabled(True)
        self.ui.cw_rotate_context.setDisabled(True)
        self.ui.close_context.setDisabled(True)
        self.ui.close_all_context.setDisabled(True)
        self.ui.info_context.setDisabled(True)
